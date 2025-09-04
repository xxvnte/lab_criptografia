from scapy.all import IP, ICMP, send, Raw
import sys
import time

def enviar_stealth_ping(mensaje, destino="8.8.8.8"):
    identificacion = 12345      
    icmp_id = 54321             
    timestamp = int(time.time()) 
    print("Campos de los paquetes enviados:")
    for i, char in enumerate(mensaje):
        payload = timestamp.to_bytes(8, 'big') + char.encode()
        pkt = IP(dst=destino, id=identificacion)/ICMP(id=icmp_id, seq=i)/Raw(payload)
        send(pkt, verbose=False)
        print(f"IP.id={identificacion} ICMP.id={icmp_id} ICMP.seq={i} Timestamp={timestamp} Payload(8b)={payload[:8].hex()} Char={char}")
    print(f"sent {len(mensaje)} packets.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python pingv4.py \"mensaje a enviar\"")
        sys.exit(1)
    mensaje = sys.argv[1]
    enviar_stealth_ping(mensaje)
    
    
    