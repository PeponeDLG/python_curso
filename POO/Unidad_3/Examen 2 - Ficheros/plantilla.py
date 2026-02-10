import os
import csv
import json


class Main:
    @staticmethod
    def main():

            os.system('clear' if os.name == 'posix' else 'cls')

    @staticmethod
    def pausa():
        input("\nPulse Enter para continuar...")            
        os.system('clear' if os.name == 'posix' else 'cls')

if __name__ == "__main__":
    Main.main()