from pc1.generate_keys_pc1 import main_func as main_func_pc1
from pc2.generate_keys_pc2 import main_funcPc2 as main_func_pc2


def main():
    flag = True
    while flag:
        print('(1) pc1')
        print('(2) pc2')
        op = int(input('Opção: '))

        if op == 1:
            main_func_pc1()
            flag = False
        elif op == 2:
            main_func_pc2()
            flag = False


if __name__ == "__main__":
    main()
