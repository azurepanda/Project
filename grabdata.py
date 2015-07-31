import pynbody
import numpy
import os

files = numpy.genfromtxt('files', dtype=str)
folders = numpy.genfromtxt('folders', dtype=str)
failed = open('failed.txt', 'a')

for j in range(9, len(folders)):
    fld = str(folders[j])
    f1 = 'angmom/vrangmom' + fld
    vrangmom = open(f1, 'a')
    for i in range(0, len(files)):
        fl = str(files[i])
#        fldst = "testing/"  + fld + '.' + fl
        fldst = "/disk2/lwang/gasoline2.1/" + fld + '/' + fld + '.' + fl
#        fldst = "testing/" + fld + '.' + fl
        try:
#            linkname = fld + '.' + fl
            linkname = '/disk2/lwang/gasoline2.1/' + fld + '/' + fld + '.' + fl
#            os.symlink(fldst, linkname)
#            param = "testing/" + fld + '.param'
#            param = "/disk2/lwang/gasoline2.1/" + fld + '/' + fld + '.param'
#            paramlink = fld + '.param'
#            os.symlink(param, paramlink)
            s = pynbody.load(linkname)
            h = s.halos()
            s.physical_units()
            # we center on the lowest potential star particle
            pynbody.analysis.halo.center(s.s, mode='pot')
            # we set up 3 spheres 1 for the stars at 10% Rvir
            # 1 for the gas at 10% Rvir
            # 1 for the dark matter at Rvir
            sph = pynbody.filt.Sphere(0.1*pynbody.analysis.halo.virial_radius(h[1]))
            sphg = pynbody.filt.Sphere(0.1*pynbody.analysis.halo.virial_radius(h[1]))
            sphd = pynbody.filt.Sphere(pynbody.analysis.halo.virial_radius(h[1]))
            vrsmass = numpy.sum(s.s[sph]['mass'])
            vrgmass = numpy.sum(s.g[sphg]['mass'])
            vrdmass = numpy.sum(h[1]['mass'])
            # we sum all the mass
            totsmass = numpy.sum(s.s['mass'])
            totgmass = numpy.sum(s.g['mass'])
            totdmass = numpy.sum(s.d['mass'])
            # we find the triaxial components of the DM halo at Rvir
            b, c, evecs = pynbody.analysis.halo.shape(h[1].d[sphd])
            a = 1
            # we calculate the angular momentum of the stars and normalise
            angmom = pynbody.analysis.angmom.ang_mom_vec_units(h[1].s[sph])
            norm = numpy.sqrt(angmom[0]**2 + angmom[1]**2 + angmom[2]**2)
            angmomvr = angmom/norm
            # we calculate the angular momenum of the gas and normalise
            angmomg = pynbody.analysis.angmom.ang_mom_vec_units(h[1].g[sphg])
            normg = numpy.sqrt(angmomg[0]**2 + angmomg[1]**2 + angmomg[2]**2)
            angmomvrg = angmomg/normg
            # we calcualte the angle between the angular mometnum of the stars and the  major, intermediate, and minor axes of the triaxial DM halo
            Ldota = angmomvr[0]*evecs[0][0]+angmomvr[1]*evecs[0][1]+angmomvr[2]*evecs[0][2]
            Ldotb = angmomvr[0]*evecs[1][0]+angmomvr[1]*evecs[1][1]+angmomvr[2]*evecs[1][2]
            Ldotc = angmomvr[0]*evecs[2][0]+angmomvr[1]*evecs[2][1]+angmomvr[2]*evecs[2][2]
            # we calculate the angle between the angular momentum of the stars and the angular momentum of the gas
            LdotLg = angmomvr[0]*angmomvrg[0]+angmomvr[1]*angmomvrg[1]+angmomvr[2]*angmomvrg[2]
            # we determine the time and redshift
            time = s.properties['time'].in_units('Gyr')
            reds = s.properties['z']
            # we sum the mass within the spheres

            # print format:
            # L*(x, y, z), Lg(x, y, z), a, b, c, Ldota, Ldotb, Ldotc, L*dotLg,
            # vrmass(*, g, d), totmass(*, g, d), time, z
            vrhold = str(angmomvr[0]) + ' ' + str(angmomvr[1]) + ' ' + str(angmomvr[2]) + ' ' + str(angmomvrg[0]) + ' ' + str(angmomvrg[1]) + ' ' + str(angmomvrg[2]) + ' ' + str(a) + ' ' + str(b) + ' ' + str(c) + ' ' + str(Ldota) + ' ' + str(Ldotb) + ' ' + str(Ldotc) + ' ' + str(LdotLg) + ' ' + str(vrsmass) + ' ' + str(vrgmass) + ' ' + str(vrdmass) + ' ' + str(totsmass) + ' ' + str(totgmass) + ' ' + str(totdmass) + ' '   + str(time) + ' ' + str(reds) + "\n"
            vrangmom.write(vrhold)
            print fldst, vrdmass
            os.remove(paramlink)
            os.remove(linkname)
        except Exception:
            failed.write(fldst)
            pass
    vrangmom.close()
failed.close()
