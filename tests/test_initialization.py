from botXsrc.botXexport import botXexport

def test_initialization():
    for module_name, module_package in botXexport.items():
        print('test initilizing ', module_name, '...')
        tmp_module = module_package['module']()
    print('done!')
