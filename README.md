# Hesiod VCF Validation
Uses [Project Hesiod](https://github.com/boconnor2017/hesiod), a Photon based approach to launch databases. 

# Prerequisites
The following binaries are **required** to run hesiod-vcf-validation:

| Requirement | Description |
|-------------|-------------|
| PhotonOS OVA | version 5.0 recommended (download from [VMware GitHub](https://vmware.github.io/photon/)) |

# Quick Start
Deploy Photon OS OVA to the physical server. Follow the steps in the [Hesiod Photon OS Quick Start](https://github.com/boconnor2017/hesiod/blob/main/photon/readme.md) readme file to prep the Photon server for this project. 

*Recommended: run these scripts as root.*
```
cd /usr/local/
```
```
git clone https://github.com/boconnor2017/hesiod-db
```
```
cp -r hesiod/python/ hesiod-db/hesiod
```
```
cd hesiod-db
```

## Launch a PostgreSQL database
```
python3 hesiod-db --postgres
```

