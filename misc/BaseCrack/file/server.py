import os

WELCOME = '''
███████╗     ██╗███╗   ██╗██╗   ██╗ ██████╗████████╗███████╗
╚══███╔╝     ██║████╗  ██║██║   ██║██╔════╝╚══██╔══╝██╔════╝
  ███╔╝      ██║██╔██╗ ██║██║   ██║██║        ██║   █████╗  
 ███╔╝  ██   ██║██║╚██╗██║██║   ██║██║        ██║   ██╔══╝  
███████╗╚█████╔╝██║ ╚████║╚██████╔╝╚██████╗   ██║   ██║     
╚══════╝ ╚════╝ ╚═╝  ╚═══╝ ╚═════╝  ╚═════╝   ╚═╝   ╚═╝     
'''
basecode = ''':.Ji;;c[%H@7O3_;JKlgAOU)a='%+49ibGC<GbK5;DD3d@olNPA85+$<`M.\<*+$0;cH5'ASX/+<(0PV@RYNZ;))*b@l%+@=%@LV=)(oZAOpc_<ED%\@8oQf9h8r;A2.7^@VSIh<,6G,=tjc6=]e9m@9$':>$,`6<,H/@=&i.%9iskX9ef+8;H-+g:KD.+A6(uQASb+.@7Y/k@V^'\9l=)h@ms.$;--pg<GP'L;_^QqAOK\"3'''
ans = "C0ngr@tu1atiOns_On_coMpleting_t3e_Ch41lenge_I_wi1l_giv4_y0u_A_ffflll444gggg!!!"
print("=============================================================")
print(WELCOME)
print("Welcome to the 2024 ZJNUCTF (*_*)")
print("Can you crack these base code (?_?)")
print("If you cracked I will give you the flag you want (^_^)")
print("=============================================================")
print("Base Code:")
print(basecode)
print("=============================================================")
data_input = input("Please input your answer:\n")
if data_input == ans:
    os.system('cat /flag')
else:
    print("Wrong Answer!!! Please Try Again @_@")
