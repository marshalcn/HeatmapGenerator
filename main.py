# -*- coding: utf-8 -*-
import sys

from PySide6 import QtCore
from PySide6.QtWidgets import QApplication, QTableWidgetItem, QFileDialog, QMainWindow
import pandas as mypd
import numpy as np
from draw_heatmap import DrawHeatmap
# 导入所画的界面
from tabledemo import *


# 自定义类
class Excel_Table(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.excelButton.clicked.connect(self.Open_Excel_File) # connect作用就是执行某个函数
        self.saveButton.clicked.connect(self.Excel_Save)

    def Open_Excel_File(self):
        excel_name = QFileDialog.getOpenFileName(self, '选择文件', '', 'Excel files(*.xlsx)')   # 过滤出xlsx格式的文件
        self.path_excel_name = excel_name[0]
        print("Excel文档的路径： ", self.path_excel_name)
        if len(self.path_excel_name) > 0:
            self.Read_Excel_Data()
            self.Table_Initialize()

    # 读取 EXCEL 文档的数据
    def Read_Excel_Data(self):
        self.excel_file = mypd.read_excel(self.path_excel_name)
        # 获取数据的行标签与列标签
        self.columns = self.excel_file.columns
        self.rows = self.excel_file.index

    # 定义表格的初始化参数
    def Table_Initialize(self):
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tableWidget.setRowCount(len(self.rows))    # 设置表格的行数
        self.tableWidget.setColumnCount(len(self.columns))  # 设置表格的列数
        self.tableWidget.setHorizontalHeaderLabels(self.columns) # 设置表格的列标签
        self.tableWidget.setGeometry(QtCore.QRect(223, 120, 1000, 800)) # 重新设置表格区域的大小
        # 将 EXCEL 文档的数据显示在表格中
        for i in range(len(self.rows)):
            for j in range(len(self.columns)):
                tstr = str(self.excel_file.iloc[i][j])
                data = QTableWidgetItem(tstr)
                self.tableWidget.setItem(i, j, data)

        self.tableWidget.resizeColumnsToContents() # 列宽随着内容调整
        self.tableWidget.resizeRowsToContents() # 行宽随着内容调整
        self.tableWidget.setAlternatingRowColors(True)  # 表格的颜色交错显示
        self.tableWidget.itemChanged.connect(self.Table_Data_Change) # 将表格中单元格改变时，触发 Table_Data_Change 事件

    # 当表格的内容改变时获取内容
    def Table_Data_Change(self, item):
        text = item.text()
        itemrow = item.row()
        itemcol = item.column()
        self.excel_file.iloc[itemrow, itemcol] = text # 使用[i][j]形式会报销


    def Excel_Save(self):
        pic_name = self.path_excel_name.replace(".xlsx", ".png")
        data, title, x_labels, y_labels = self.get_table_data_labels()
        print("file name :" + pic_name)

        heatmap = DrawHeatmap(data=data, title=title, path=pic_name, x_labels=x_labels, y_labels=y_labels)
        heatmap.mk_pics()
        self.excel_file.to_excel(self.path_excel_name, index=False)

    def get_table_data_labels(self):
        row_num = len(self.rows)
        title = ''
        r_labels = []
        c_labels = []
        for c, v in enumerate(self.excel_file.columns.values):
            if c == 0:
                title = v
                continue
            try:
                c_labels.append(v)
            except Exception as e:
                print(e)
                continue
        for r in range(row_num):
            try:
                r_labels.append(self.excel_file.iloc[r].iat[0])
            except Exception as e:
                print(e)
                continue
        data = self.excel_file[c_labels]
        temp = np.zeros(data.shape)
        temp = mypd.DataFrame(temp)
        for i, row in enumerate(data.values):
            for j, v in enumerate(row):
                temp.iloc[i, j] = data.iloc[i, j]
        return temp, title, c_labels, r_labels


if __name__ == '__main__':
    app = QApplication(sys.argv)
    excelTable = Excel_Table()
    excelTable.show()
    sys.exit(app.exec())
