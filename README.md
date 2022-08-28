# Blockchain
Create a blockchain based on a (Proof of work) algorithm

* Calculate proof of work
* Reward miners (one transactions)
* Creation of the new block and add it to the chain
* API Rest
** POST /transactions/new new transactions to add to the next block
** GET /mine create a new block
** GET /chain information abount the full blockchain

Notes: require memcached and python3-memcache library

```
# Debian
apt install memcached python3-memcache

systemctl enable --now memcached

# checking
netstat -putan | grep 11211
```

## Usage
Debug is enable by default.

```
python3 index.py -d
```

Using curl
```
# Check blockchain
curl http://localhost:8000/chain

# New transaction
curl -X POST \
     -H 'Content-Type: application/json' \
     -d '{"sender": "0xffdc12344", "recipient": "", "amount": 0.5421}' \
     http://localhost:8000/transaction/new

# Solve a block
curl http://localhost:8000/mine
```
