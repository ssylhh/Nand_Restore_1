# This Python file uses the following encoding: utf-8
import sys
import configparser

from PySide6.QtWidgets import QApplication, QMainWindow, QCheckBox, QMessageBox
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
        
        # self.ping_ip()
        # threading.Thread(target=self.ping_ip, daemon=True).start()
        self.start_ping_thread()  


        # self.current_dir = os.path.dirname(os.path.abspath(__file__))
        
        if getattr(sys, 'frozen', False):             
            self.current_dir = os.path.dirname(sys.executable)
        else:          
            self.current_dir = os.path.dirname(os.path.abspath(__file__))        
    
    
        # dll_path = os.path.join(self.current_dir, "K23A_YB_x64.dll")
        # self.my_dll = MyDllWrapper(dll_path)

        self.dll_path = self.find_any_dll()

        if not self.dll_path:
            return  

        try:
            self.my_dll = MyDllWrapper(self.dll_path)
        except Exception as e:
            QMessageBox.critical(self, "DLL 로드 오류", f"DLL을 로드하는 중 오류 발생:\n{str(e)}")
            return           
        

        self.ui.all_load.clicked.connect(lambda: self.all_load())    
        
        # self.ui.checkBox12.stateChanged.connect(self.on_checkbox12_changed)   
        # self.ui.checkBox12.stateChanged.connect(lambda state: self.on_checkbox12_changed(state))     
        # self.ui.checkBox12.clicked.connect(lambda: self.on_checkbox12_clicked())
       
        self.connect_gridLayout_checkboxes()
        self.load_dll_filename_to_ui()
        self.load_ini_info()

    def find_any_dll(self):
        
        dll_files = [f for f in os.listdir(self.current_dir) if f.lower().endswith('.dll')]

        if not dll_files:
            QMessageBox.critical(self, "No Dll files", " DLL file not available!\n"
                                  "Position DLL file at the same directory.")
            return None
        
        selected_dll = dll_files[0] 
        QMessageBox.information(self, "DLL Loading", f"Next DLL will be loaded\n{selected_dll}")
        return os.path.join(self.current_dir, selected_dll)


    def start_ping_thread(self):
        threading.Thread(target=self.ping_ip, daemon=True).start()

    def load_ini_info(self):
        
        ini_file = self.find_ini_file()
        
        if ini_file:
            name_value = self.parse_ini_file(ini_file, "ASIC_Info")
            
            if name_value:
                self.ui.INI_info.setText("ASIC : " + name_value)
            else:
                self.ui.INI_info.setText("ASIC info. Not available")
        else:
            self.ui.INI_info.setText("INI File N.A.")

    def find_ini_file(self):
        
        for file in os.listdir(os.getcwd()):
            if file.endswith(".ini"):
                return file  
        return None
   

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
            self.ui.DLLName.setText("DLL Name : No DLL file")
            return
        elif len(dll_files) > 1:
            # QMessageBox.critical(self, "오류", "DLL 파일이 2개 이상 존재합니다. 하나만 있어야 합니다.")
            self.ui.DLLName.setText("DLL Name : two more DLL files")
            return
       
        self.ui.DLLName.setText("DLL Name : " + dll_files[0])


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


    # def ping_ip(self, timeout=120, buffer_size=32):
    #     # ip_address = "10.106.14.73"
    #     ip_address = "192.168.0.7"
        
    #     try:
    #         response_time = ping(ip_address, timeout=timeout, size=buffer_size)

    #         if not response_time:  
    #             error_msg = "Ping failed: No response"
    #         else:
    #             response_time *= 1000  # Convert to milliseconds
    #             self.ui.tcp_status_label.setText(f"status: success\nresponse_time_ms: {response_time}")
    #             return {"status": "success", "response_time_ms": response_time}

    #     except Exception as e:
    #         error_msg = f"Ping failed: {str(e)}"
       
    #     self.ui.tcp_status_label.setText(f"status: failure\nerror: {error_msg}")
    #     return {"status": "failure", "error": error_msg}            
 
    def ping_ip(self, timeout=120, buffer_size=32):
        ip_address = "192.168.0.7"

        while True:
            try:
                response_time = ping(ip_address, timeout=timeout, size=buffer_size)

                if response_time:  
                    response_time *= 1000  # Convert to milliseconds
                    # self.ui.tcp_status_label.setText(f"status: success\nresponse_time_ms: {response_time}")
                    self.update_ui(status="success", response_time=response_time)
                    return  

            except Exception as e:
                error_msg = f"Ping failed: {str(e)}"

            # self.ui.tcp_status_label.setText(f"status: failure\nRetrying in 5 seconds...")  
            self.update_ui(status="failure", error=None)          
            time.sleep(5)  
            
    def update_ui(self, status, response_time=None, error=None):
        
        if status == "success":
            self.ui.tcp_status_label.setText(f"status: success\nresponse_time_ms: {response_time}")
            self.ui.tcp_status_label.setStyleSheet("color: green;")      
            self.ui.all_load.setStyleSheet("background-color: lightgreen; color: black;")        
        else:
            self.ui.tcp_status_label.setText(f"status: failure\nRetrying in 5 seconds...")
            self.ui.tcp_status_label.setStyleSheet("color: red;")  
            self.ui.all_load.setStyleSheet("background-color: red; color: white;")             
            
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
        # self.ui.tcp_status_label.setText(f"Checked: {bin(checked_options)}")       
        
        
#        errcode = self.my_dll.k23_all_load("NAND_RESTORE\0", self.current_dir + "\0", 0 , True)
#        print(f'all_load errcode = {errcode}')   


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())

