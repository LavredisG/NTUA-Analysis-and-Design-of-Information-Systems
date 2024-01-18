# NTUA-Analysis-and-Design-of-Information-Systems
This is a repo for the "Analsysis and Design of Information Systems" Project (2023-2024), which compares 2 timeseries databases, InfluxDB and TimescaleDB.

The following instructions set up the project in
Ubuntu 16.04 machines. If that's not the case, links
for the respective guides are provided below to support
your machine.

<ul>
  <li><a href="https://docs.timescale.com/self-hosted/latest/install/"> TimescaleDB (v2.4.0) (single node version) </a></li>
  <li><a href="https://docs.influxdata.com/influxdb/v1/introduction/download/"> InfluxDB v1 OSS (v1.8.10) </a></li>
  <li><a href="https://www.postgresql.org/download/"> PostgreSQL 13 </a></li>
  <li><a href="https://go.dev/doc/install"> Golang (v.1.21.6) </a></li>
</ul>

## Setup

### 1. Download and Install tools and databases
```bash
# Update your system
sudo apt-get update
sudo apt-get upgrade

# Install wget package manager
sudo apt-get install wget

# Download and install InfluxDB (v1.8.10)
wget https://dl.influxdata.com/influxdb/releases/influxdb_1.8.10_amd64.deb
sudo dpkg -i influxdb_1.8.10_amd64.deb
sudo service influxdb start

# Download and install Postgres 13
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
echo "deb http://apt-archive.postgresql.org/pub/repos/apt/ $(lsb_release -cs)-pgdg main" | sudo tee /etc/apt/sources.list.d/pgdg.list
sudo apt-get update
sudo apt-get install postgresql-13
sudo -u postgres psql -c "SELECT version();" # Verify installation

# Download and install TimescaleDB
sudo add-apt-repository ppa:timescale/timescaledb-ppa
sudo apt-get update
sudo apt-get install timescaledb-2-postgresql-13
sudo timescaledb-tune
sudo service postgresql restart

#Download and install Go (v.1.21.6)
wget https://golang.org/dl/go1.21.6.linux-amd64.tar.gz
sudo tar -C /usr/local -xzf go1.21.6.linux-amd64.tar.gz
```

### 2. Set environment variables for Go workspace
```bash
# Go binaries, source files etc are located in /usr/local/go
# Set these environment variables in ~/.bashrc
echo 'export PATH=$PATH:/usr/local/go/bin' >> ~/.bashrc
echo 'export GOPATH=$HOME/go' >> ~/.bashrc
echo 'export PATH=$PATH:$GOPATH/bin' >> ~/.bashrc
echo 'export GOROOT=/usr/local/go' >> ~/.bashrc
source ~/.bashrc
```
Your Go workspace should now be set up and look like this:
(the repo that we will work in *(TSBS)* will be cloned where project1 is, under src)

![Go workspace](Go_workspace.PNG)

### 3. Clone TSBS suite
```bash
cd $GOPATH/src
git clone https://github.com/timescale/tsbs.git
cd tsbs
make
```



