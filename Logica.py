from logic import *

def logica_He(orientacion_sexual_mia,genre_mio,orientacion_sexual_otro,genre_user):
    Pref_fija = Symbol(orientacion_sexual_mia)
    pref = Symbol("heterosexual")
    Genre_fij = Symbol(genre_mio)
    orientacion_sexual_ac = Symbol("orientacion sexual")
    gen = Symbol("a")
    conocimiento1 = And(Pref_fija,pref,orientacion_sexual_ac)
    conocimiento2 = And(Genre_fij,gen)
    gen = Symbol(genre_user)
    orientacion_sexual_ac = Symbol(orientacion_sexual_otro)
    genree = model_check(conocimiento2,gen)
    esta = model_check(conocimiento1,orientacion_sexual_ac)
    return genree, esta

def logica_Ho(preferencias_mio,genre_mio,estado_civil,genre_user):
    Pref_fija = Symbol(preferencias_mio)
    pref = Symbol("homosexual")
    Genre_fij = Symbol(genre_mio)
    estado_civil_ac = Symbol("est_civil")
    gen = Symbol("a")
    conocimiento1 = And(Pref_fija,pref,estado_civil_ac)
    conocimiento2 = And(Genre_fij,gen)
    gen = Symbol(genre_user)
    estado_civil_ac = Symbol(estado_civil)
    genree = model_check(conocimiento2,gen)
    esta = model_check(conocimiento1,estado_civil_ac)
    return genree, esta
    
def estSol(pref_estado):
    pref = Symbol("casado")
    pf = Symbol("estado")
    conocimiento = And(pref,pf)
    pf = Symbol(pref_estado)
    return model_check(conocimiento,pf)

def estDiv(pref_estado):
    pref1 = Symbol("casado")
    pref2 = Symbol("viudo")
    pf = Symbol("estado")
    conocimiento = And(pf,Or(pref1,pref2))
    pf = Symbol(pref_estado)
    return model_check(conocimiento,pf)

def estViu(pref_estado):
    pref1 = Symbol("casado")
    pref2 = Symbol("divorciado")
    pf = Symbol("estado")
    conocimiento1 = And(pref2,pf)
    conocimiento2 = And(pref1,pf)
    pf = Symbol(pref_estado)
    di = model_check(conocimiento1,pf)
    ca = model_check(conocimiento2,pf)
    return di,ca