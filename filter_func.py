def filter_injections(mass1, mass2, spin1z, spin2z):
    """Filter injections according to O2 requirements.

    Taking mass1, mass2, spin1z, spin2z return a boolean array which is True
    if point is within the O2 template region and False if it is outside the
    O2 template region. Currently using the PyCBC definition, but this can
    always be updated.
    """
    import numpy
    from scipy.interpolate import UnivariateSpline
    from lalinspiral.sbank.waveforms import SEOBNRv4ROMTemplate, TaylorF2Template, IMRPhenomDTemplate
    ifo_data = numpy.loadtxt('/home/marion.pillas/projects/template_bank/aligo_O4low.txt')
    f_orig, asddata = ifo_data[:,0], ifo_data[:,1]
    psddata = numpy.square(asddata)
    interpolator = UnivariateSpline(f_orig, numpy.log(psddata), s=0)
    noise_m = lambda u,g: numpy.where(g < 1024, numpy.exp(interpolator(g)), numpy.inf)

    class Dummy(object):
        flow = 15.
        fhigh_max = 1024
        noise_model = noise_m
        optimize_flow = 0.995
        
    bank = Dummy()
    outs = []
    for i in range(len(mass1)):
        t = SEOBNRv4ROMTemplate(mass1[i], mass2[i], spin1z[i], spin2z[i],
                               bank=bank)
        if t.dur > 0.15:
            outs.append(True)
        else:
            outs.append(False)
    return outs
    
