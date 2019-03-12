import numpy as np
import math

dk = np.float64(0.05)
max_k = 15 / dk

def blip(temp):
    eps =  1 / temp
    dr = np.float64(1.0) / 50000
    a_dss = np.float64(0.0)

    if temp <= 0.0000001:
        a_dss = np.float64(1.0)
    else :
        r = dr
        while r <= 1:
            a_dss = a_dss + dr * r  * r * math.exp(-eps * (1.0 / math.pow(r,12) - 2.0 / math.pow(r, 6) + 1))
            r = r + dr
        a_dss = math.pow(1 - 3 * a_dss, 1 / 3.0)
    return a_dss


def calc(a_temp, a_phi, end_temp):
    a_dss = blip(a_temp)
    phi_initial = a_phi * math.pow(a_dss, 3)
    print(phi_initial)
    sk_initial = calc_sk(phi_initial)
    a_dss = blip(end_temp)
    end_phi = a_phi * math.pow(a_dss,3)


def calc_sk(a_phi):
    sk = []
    sk.append(1 / (1.0 - a_phi * (a_phi * a_phi * a_phi - 4 * a_phi * a_phi  + 2 * a_phi - 8) / math.pow(1 - a_phi, 4)))
    i = 1
    while i < max_k :
        k  = i * dk
        p0 = 3 * a_phi * (math.pow(k, 2)  * math.pow(2 + a_phi, 2) + 4 * math.pow(1 + 2 * a_phi , 2))
        p1 = -12 * a_phi * math.pow(1 + 2 * a_phi, 2)  +  k * k * (1 - 6 * a_phi + 5 * math.pow(a_phi, 3))
        p2 = -12 * a_phi * math.pow(1 + 2 * a_phi, 2)  + 3 * a_phi * k * k * (-2 + 4 * a_phi + 7  * a_phi * a_phi) - (math.pow(k, 4) / 2.0 ) * (2 - 3 * a_phi + math.pow(a_phi, 3))
        ck = (np.float64(-24.0) * a_phi / (math.pow(k, 6) * math.pow(1- a_phi, 4))) * (p0 + p1 * k * math.sin(k) + p2 * math.cos(k))
        sk.append(1 / (np.float64(1.0) - ck))
        i = i + 1
    return sk


if __name__ == "__main__":
    calc(np.float64(6.5431891), np.float64(0.573))


# void blip(double temp, double *a_dss){
#     double eps, dr;

#     eps = 1 / temp;
#     dr = 1.00 / 50000;
#     (*a_dss) = 0;
#     if(temp <= 0.0000001){
#         (*a_dss) = 1;
#     }else{
#         for(double r = dr; r <= 1 ; r += dr){
#             (*a_dss) = (*a_dss) + dr * r * r * exp(-eps * (1.0/pow(r, 12) - 2.0 / pow(r, 6) + 1));
#         }
#         (*a_dss) = pow(1 - 3 * (*a_dss), 1/3.0);
#     }
# }
