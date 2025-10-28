import time


class Network:
    #Shows how the flow of communication occurs
    def send(self, sender, receiver, message):
        print(f"[Network] {sender} -> {receiver}: {message}")


#DHCP Simulation
class DHCPServer:
    def __init__(self, ip_pool_start="192.168.1.2", ip_pool_end="192.168.1.10"):
        self.ip_pool = self.generate_pool(ip_pool_start, ip_pool_end)
        self.assigned = {}

    def generate_pool(self, start, end):
        s = int(start.split('.')[-1])
        e = int(end.split('.')[-1])
        base = '.'.join(start.split('.')[:-1])
        return [f"{base}.{i}" for i in range(s, e + 1)]

    def handle_discover(self, client):
        print(f"[DHCP] DISCOVER from {client.name}")
        offer_ip = self.ip_pool.pop(0)
        self.assigned[client.name] = offer_ip
        print(f"[DHCP] OFFER -> {client.name}: {offer_ip}")
        return offer_ip

    def handle_request(self, client, requested_ip):
        print(f"[DHCP] REQUEST from {client.name} for {requested_ip}")
        assigned_ip = self.assigned.get(client.name)
        if assigned_ip == requested_ip:
            print(f"[DHCP] ACK -> {client.name}: {assigned_ip}")
            return assigned_ip
        else:
            print(f"[DHCP] NAK -> {client.name}")
            return None


#DNS Simulation
#DNS Server
class DNSServer:
    def __init__(self):
        self.records = {}

    def register(self, name, ip):
        self.records[name] = ip
        print(f"[DNS] Registered {name} -> {ip}")

    def resolve(self, name):
        ip = self.records.get(name)
        if ip:
            print(f"[DNS] Query {name} -> {ip}")
        else:
            print(f"[DNS] Query {name} -> Not found")
        return ip


#DNS Client
class Client:
    def __init__(self, name, network, dhcp, dns):
        self.name = name
        self.network = network
        self.dhcp = dhcp
        self.dns = dns
        self.ip = None

    def boot(self):
        print(f"\n--- {self.name} Booting ---")
        self.network.send(self.name, "DHCP Server", "DHCP DISCOVER")
        offer_ip = self.dhcp.handle_discover(self)
        self.network.send(self.name, "DHCP Server", f"DHCP REQUEST ({offer_ip})")
        self.ip = self.dhcp.handle_request(self, offer_ip)
        self.dns.register(f"{self.name}.local", self.ip)

    def ping(self, target_name):
        print(f"\n[{self.name}] wants to ping {target_name}")
        ip = self.dns.resolve(target_name)
        if ip:
            self.network.send(self.name, target_name, f"PING (to {ip})")
            print(f"[{target_name}] PONG ← {self.name}")
        else:
            print(f"[{self.name}] Ping failed: target not found")


#Work Flow

network = Network()
dhcp_server = DHCPServer()
dns_server = DNSServer()

clientA = Client("clientA", network, dhcp_server, dns_server)
clientB = Client("clientB", network, dhcp_server, dns_server)

# Simulate startup
clientA.boot()
time.sleep(1)
clientB.boot()
time.sleep(1)

# Simulate communication
clientA.ping("clientB.local")
