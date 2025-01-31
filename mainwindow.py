# This Python file uses the following encoding: utf-8
import sys
import configparser

from PySide6.QtWidgets import QApplication, QMainWindow, QCheckBox
# from PySide6.QtCore import Qt
import os
import threading

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow
import socket
import time
from ping3 import ping, verbose_ping
from dll_wrapper import MyDllWrapper

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.initial_setup() 

    def initial_setup(self):

        self.gridLayout = self.ui.gridLayout
        self.lineEdit = self.ui.lineEdit_3
        
        # self.ping_ip()
        threading.Thread(target=self.ping_ip, daemon=True).start()

        self.current_dir = os.path.dirname(os.path.abspath(__file__))
        dll_path = os.path.join(self.current_dir, "K23A_YB_x64.dll")

        self.my_dll = MyDllWrapper(dll_path)

        self.ui.all_load.clicked.connect(lambda: self.all_load())    
        
        # self.ui.checkBox12.stateChanged.connect(self.on_checkbox12_changed)   
        # self.ui.checkBox12.stateChanged.connect(lambda state: self.on_checkbox12_changed(state))     
        # self.ui.checkBox12.clicked.connect(lambda: self.on_checkbox12_clicked())
       
        self.connect_gridLayout_checkboxes()
        self.load_dll_filename_to_ui()
        self.load_ini_to_lineEdit()

    def load_ini_to_lineEdit(self):
        
        ini_file = self.find_ini_file()
        
        if ini_file:
            name_value = self.parse_ini_file(ini_file, "ASIC_Info")
            
            if name_value:
                self.lineEdit.setText(name_value)
            else:
                self.lineEdit.setText("Not available")
        else:
            self.lineEdit.setText("File N.A.")

    def find_ini_file(self):
        
        for file in os.listdir(os.getcwd()):
            if file.endswith(".ini"):
                return file  
        return None

    # def parse_ini_file(self, ini_file, key_name):
       
    #     config = configparser.ConfigParser()
    #     config.read(ini_file, encoding='utf-8')

    #     for section in config.sections():
    #         if key_name in config[section]:  # 특정 key 포함 여부 확인
    #             return config[section][key_name]  
    #     return None        

    def parse_ini_file(self, ini_file, key_name):
     
        # config = configparser.ConfigParser(strict=False)
        config = self.read_ini_ignore_percent(ini_file)
        # config.read(ini_file, encoding='utf-8')
         
        for section in config.sections():
            if key_name in config[section]:  
                value = config[section][key_name]
                
                if "%" in value:
                    value = value.split("%")[0].strip()  # % 앞부분만 남기고 공백 제거

                return value  

        return None 

    def read_ini_ignore_percent(self, ini_file):
        with open(ini_file, "r", encoding="utf-8") as f:
            lines = f.readlines()            
            
        filtered_lines = [line for line in lines if not line.strip().startswith("%")]
        # config = configparser.ConfigParser()
        config = configparser.ConfigParser(interpolation=None)
        config.read_string("".join(filtered_lines))
        return config


    def load_dll_filename_to_ui(self):

        current_dir = os.getcwd()  
        dll_files = [f for f in os.listdir(current_dir) if f.endswith('.dll')]

        if len(dll_files) == 0:
            # QMessageBox.critical(self, "오류", "DLL 파일이 존재하지 않습니다.")
            self.ui.lineEdit_2.setText("No DLL file")
            return
        elif len(dll_files) > 1:
            # QMessageBox.critical(self, "오류", "DLL 파일이 2개 이상 존재합니다. 하나만 있어야 합니다.")
            self.ui.lineEdit_2.setText("two more DLL files")
            return
       
        self.ui.lineEdit_2.setText(dll_files[0])


    def connect_gridLayout_checkboxes(self):
        for row in range(self.gridLayout.rowCount()):
            for col in range(self.gridLayout.columnCount()):
                item = self.gridLayout.itemAtPosition(row, col)
                if item:
                    widget = item.widget()
                    if isinstance(widget, QCheckBox):
                        if widget.objectName() == "checkBox12":
                            widget.stateChanged.connect(self.on_checkbox12_changed)  # 특정 메서드 호출
                        else:
                            widget.stateChanged.connect(self.on_checkbox_changed)  # 기본 메서드 호출


    def ping_ip(self, timeout=120, buffer_size=32):
        # ip_address = "10.106.14.73"
        ip_address = "192.168.0.7"
        # try:
        #     response_time = ping(ip_address, timeout=timeout, size=buffer_size)

        #     print(f'response_time = {response_time}')

        #     if response_time is None:
        #         self.ui.tcp_status_label.setText("status: failure\nerror: Request timed out")
        #         return {
        #             "status": "failure",
        #             "error": "Request timed out"
        #         }                
        #     else:
        #         response_time = response_time * 1000
        #         self.ui.tcp_status_label.setText(f"status: success\nresponse_time_ms: {response_time}")
        #         return {
        #             "status": "success",
        #             "response_time_ms": response_time  # Convert to milliseconds
        #         }
        # except Exception as e:
        #     return {
        #         "status": "failure",
        #         "error": str(e)
        #     }
        try:
            response_time = ping(ip_address, timeout=timeout, size=buffer_size)

            if not response_time:  
                error_msg = "Ping failed: No response"
            else:
                response_time *= 1000  # Convert to milliseconds
                self.ui.tcp_status_label.setText(f"status: success\nresponse_time_ms: {response_time}")
                return {"status": "success", "response_time_ms": response_time}

        except Exception as e:
            error_msg = f"Ping failed: {str(e)}"
       
        self.ui.tcp_status_label.setText(f"status: failure\nerror: {error_msg}")
        return {"status": "failure", "error": error_msg}            
            
            
    # def on_checkbox12_changed(self, state): 
    def on_checkbox12_changed(self):
        
        # if state == Qt.Checked:  
        if self.ui.checkBox12.isChecked():
            print("checkBox12 checked....other checkbox disabled")

            for i in range(1, 12):  
                checkbox = getattr(self.ui, f'checkBox{i}')
                checkbox.blockSignals(True)  # 시그널 차단
                checkbox.setChecked(False)  
                checkbox.blockSignals(False)  # 시그널 다시 활성화           
         
            print("모든 체크박스가 해제됨.")
        
    def on_checkbox_changed(self):
        
        if self.ui.checkBox12.isChecked():
            print("checkBox12 disabled")

            self.ui.checkBox12.setChecked(False)               
    

    def all_load(self):
        
        checked_options = 0b000000000000  

        if self.ui.checkBox1.isChecked():
            checked_options |= 0b000000000001  
        if self.ui.checkBox2.isChecked():
            checked_options |= 0b000000000010  
        if self.ui.checkBox3.isChecked():
            checked_options |= 0b000000000100  
        if self.ui.checkBox4.isChecked():
            checked_options |= 0b000000001000  
        if self.ui.checkBox5.isChecked():
            checked_options |= 0b000000010000  
        if self.ui.checkBox6.isChecked():
            checked_options |= 0b000000100000                          
        if self.ui.checkBox7.isChecked():
            checked_options |= 0b000001000000  
        if self.ui.checkBox8.isChecked():
            checked_options |= 0b000010000000  
        if self.ui.checkBox9.isChecked():
            checked_options |= 0b000100000000  
        if self.ui.checkBox10.isChecked():
            checked_options |= 0b001000000000  
        if self.ui.checkBox11.isChecked():
            checked_options |= 0b010000000000  
        if self.ui.checkBox12.isChecked():
            checked_options = 0b000000000000                       
            

        print(f"Checked Options (Binary): {bin(checked_options)}")
        print(f"Checked Options : {checked_options}")
        self.ui.tcp_status_label.setText(f"Checked: {bin(checked_options)}")       
        
        
#        errcode = self.my_dll.k23_all_load("NAND_RESTORE\0", self.current_dir + "\0", 0 , True)
#        print(f'all_load errcode = {errcode}')   


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())

