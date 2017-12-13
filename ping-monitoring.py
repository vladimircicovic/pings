import pings

#TODO: lokalno ili remote monitoring
#TODO: kopiranje preko ssh, konfiguracija agenta, namjestanje, provjera da li ima python3
#TODO: radi uptime, prosjecnu vrijednost
#TODO: grafikon - najniza,najvisa
#TODO: cuva podatke u fajlu (yaml,json, XML)


p = pings.Ping()
response = p.ping("google.com",times=2)
print(response.avg_rtt)
print(response.is_reached())
print(response.packet_size)

#print(response.print_messages())
