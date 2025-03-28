from lightning_client.client import LightningClient
import os


charlie = LightningClient(
    rpc_port=10003,
    cert_path=os.path.expanduser('~/Library/Application Support/Lnd/tls.cert'),
    macaroon_path=os.path.expanduser('~/repos/lightning-ai/dev/charlie/data/chain/bitcoin/simnet/admin.macaroon')
)

print(charlie.list_channels())
print(charlie.list_peers())