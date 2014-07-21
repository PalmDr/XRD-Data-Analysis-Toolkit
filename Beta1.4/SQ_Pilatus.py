__author__ = 'j'

# execfile("c:\\myfiles\\PCBM_SVA_1.py")

# there are a few objects which are automatically visible in WxDiff Python scripts:
# wx: module WxPython - so you can create Messages with wx.MessageBox('Hello there.'. 'Greeting')
# wxdiff_api: this is the api exposed by the WxDiff program - all the good stuff happens here.
# MDIRoot: the root MDI Frame object of the program
# MDIParent: the same
# wxdiffwd_list: list of open diffraction image windows - in case a script needs to manipulate an already opened one

import os
import glob
# import wxdiff_api

def SQ_Pilatus(marfilelist, LaB6_calibfile, picfilefolder):
    for filename in marfilelist:
        dim = wxdiff_api.wxdiff_diffimage(MDIRoot) # generate diffraction image object
        if dim.fromfile(filename, filetypestr='Pilatus 300K TIFF', calibfname=LaB6_calibfile, maskfname=None, wdtitle=None, interactive=False): # open image from file

            dim0 = dim.convert_region_to_qxyqz(wholeimage = True) # this converts and returns a new wxdiff_api.wxdiff_diffimage object with which you can continue to work
            dim.close() # close uncorrected image to save space
            if dim0 is not None:
                picfilename = picfilefolder + os.path.basename(filename)

                X1, Y1 = dim0.get_XY_from_QChi(Q = 0.83, Chi = -2.8)
                X2, Y2 = dim0.get_XY_from_QChi(Q = 4.9, Chi = 3.8)
                cake1 = dim0.add_cakeseg(X1, Y1, X2, Y2)
                dim0.save_to_png(fname = picfilename + 'place 1.png')
                cake1a = cake1.convert_to_qchi()
                cake1a.save_to_png(fname = picfilename + 'cake1.png')
                cake1Chidata = cake1a.column_sum()
                #cake1Chidata.save_to_png(fname = picfilename + 'cake1_Chi_data.png')
                cake1Chidata.save_to_csv(fname = picfilename + '.csv')
                #cake1fit = cake1Chidata.fit_gaussian()
                #print cake1fit
                cake1a.close()
                cake1Chidata.close()



                dim0.save_to_png(fname = picfilename + 'whole image cake.png')

                dim0.close()

            else:
                print("Error: diffraction file ") #+ dim0.diffimage.fname +" is not calibrated!"
        else:
            print("Error: cannot open ") + filename + " in script mode!"