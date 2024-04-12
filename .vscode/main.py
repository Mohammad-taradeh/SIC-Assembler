# Welcome to the SIC project for the Systems Programming course
# Supervised by: Dr. Yousef Salah
# Group canditates:
# Mohammad Taradeh - 201160

import re
import ToolsFile
import pass_one
import pass_two

mainArray = ToolsFile.appendall()
print("PRGNAME: ", ToolsFile.ProgName())
print("---------")
print("nPRGLTH: ", str(ToolsFile.ProgLength()).zfill(6))
print("----------")
# print(mainArray)
pass_one.locationCounter()
pass_one.SymbolTable()
pass_two.ObjectCode()
pass_two.HTE_Record()