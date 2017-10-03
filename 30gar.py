#!/usr/bin/python2.7
nakh = int(raw_input("Rozi Chand Nakh mikeshi ~> "))
pol = int(raw_input("cheghad baraye har nakh midi?(toman).example : 250 ~> "))
roz = int(raw_input("chand roz dar hafte mikeshi ~> "))
if roz>7:
    print "Hafte 7 Roze ha :)"
    exit()
time = int(raw_input("har nakh ro to chand daqiqe mikeshi ~> "))
kole_pol_dar_yek_roz = nakh*pol
kole_time_dar_yek_roz = nakh*time
mah = roz*4
nakh_dar_mah = mah*nakh
time_dar_mah_M = time*nakh_dar_mah
time_dar_mah_H = time*nakh_dar_mah/60
kole_pol_dar_yek_mah = pol*nakh_dar_mah
nakh_dar_sal = nakh_dar_mah*12
time_dar_sal_M = time*nakh_dar_sal
time_dar_sal_H = time*nakh_dar_sal/60
time_dar_sal_d = time_dar_sal_H/24
pol_dar_sal = kole_pol_dar_yek_mah*12
####Print
#Day
print "\n\nDay : "
print "\t[+] shoma dar har roz ", kole_pol_dar_yek_roz, "toman baraye SIGAR midahid!"
print "\tva ", kole_time_dar_yek_roz, "baraye SIGAR keshidan vaghte khod ro moatal mikoid!"
#Month
print "\n\nMonth : "
print "\t[+] shoma dar har mah ", kole_pol_dar_yek_mah,"Toman baraye SIGAR midahid!"
print "\tva ", time_dar_mah_M,"daqiq baraye SIGAR keshidan vaghte khod ro moatal mikoid! Ya behtar begam ", time_dar_mah_H,"Saat Ro Talaf mikonid ;)"
#Year
print "\n\nYear : "
print "\t[+] shoma dar har sal ", nakh_dar_sal, "Nakh SIGAR mikeshid!"
print "\tva ", pol_dar_sal,"Toman Barayash Kharj mikonid."
print "\tva ", time_dar_sal_M,"Daqiqe ya Behtar Konamesh ", time_dar_sal_H,"Saat ya hata ", time_dar_sal_d,"Roz Ro baraye Sigar keshidan Mizarid(Poshte Ham Va Bedone Moatali.)"
print "\t[-] Jalebe Na? :) Pol, Time, Zibai va az hame mohem Tar SALAMATI khodetono be khatar mindazid :) "
#Coded Py https://github.com/pouya-abbasian
