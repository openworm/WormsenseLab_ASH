from os import listdir

readme = '# Example datasets converted to NWB format\n'
readme+='\n'
main = '\n\n'
files = sorted(listdir('.'))
for f in files:
    if f.endswith('.nwb'):
        ref = f.split('.')[0]
        print('Adding %s'%f)
        readme+=' [%s](#%s) |'%(ref,ref)
        main+='## %s \n'%(ref)
        main+='![%s](%s.png) \n'%(ref,ref)
        main+='[NWB file containing data](%s.nwb) | \n'%(ref)
        main+='[View on NWB Explorer on Open Source Brain](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://github.com/openworm/WormsenseLab_ASH/raw/main/test_data/%s.nwb) \n'%(ref)
        main+='\n\n'

rmd = open('README.md','w')
rmd.write(readme[:-1])
rmd.write(main)
rmd.close()
