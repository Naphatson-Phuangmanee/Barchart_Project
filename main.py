from barchart_manager import BarChartManager

bsm = BarChartManager(1200, 700)
bsm.draw_barchart_using_sample_data()

while True:
    print()
    print('Options')
    print('[1] Draw a barchart using data from a text file')
    print('[2] Draw a barchart using manually provided data')
    print('[3] Exit')
    option = input('Select an option: ')
    print()
    if option == '1':
        bsm.draw_barchart_using_data_from_file()
    elif option == '2':
        bsm.draw_barchart_using_data_from_user_input()
    else:
        break

print('Goodbye')
bsm.close()
