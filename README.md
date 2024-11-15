Linea is a scalable Layer 2 blockchain network built on Ethereum, designed to enhance transaction speed and lower costs while maintaining Ethereum's robust security. 
Linea is planning an airdrop campaign to award their users. They are distributing Linea Voyage XP (LXP) tokens to user wallets, which is an ERC-20 token you can receive for participating in the Linea Voyage — a series of community events where you use various elements of the Linea ecosystem to help us test, grow, and build.
In this project, I segmented users using their activiy on the blockchain, including LXP points.

Dataset Information
wallet: Unique wallet of each user 
current lxp: LXP distributed to each wallet 
num_quests: Number of quests 
on_farcaster: Information if user have a farcaster account
fid: Farcaster user id
fname: Farcaster nickname
connected_wallets: Other wallet address connected to wallet
l14d_active_tier: ?
num_followers: Number of followers
num_onchain_txns: Count of transactions on linea
days_old_onchain: Active days on linea
nft_volume_usd: NFT trade volume on linea
dex_volume_usd: Decentralized exchange trade volume on linea
contracts_deployed: Number of contracts deployed on linea
times_contracts_called: Number of contracts called on linea

For customer segmentation, I selected the variables as "current lxp","dex_volume_usd","num_onchain_txns","days_old_onchain.
Scaled these variables between 0 and 1 for k-means clustering.
Elbow plot specified the optimum number of clusters as k=7.
![elbow_plot](https://github.com/user-attachments/assets/a1dc2ea7-e894-4800-81a3-a311ef911150)

For k=7, there were 3 clusters with 1 user so I redefined cluster number as k=5.

For k=5, there were 2 clusters with 1. Examining variables, I placed 2 clusters to the closest cluster and obtained 3 clusters as most active, active and normal users.

![current_lxp](https://github.com/user-attachments/assets/8e02d43d-e06e-424a-afda-4cc7cef1ecc6)
![days_old_onchain](https://github.com/user-attachments/assets/c9e2e5c8-4a61-4bf0-80a9-c4c42179ce49)
![dex_volume](https://github.com/user-attachments/assets/dd99f0a5-995c-403d-9915-61e9d15a4086)
![num_onchain_tx](https://github.com/user-attachments/assets/081d174e-1533-4696-989a-81f280820238)

Comments:
I used sql queries in Dune Analytics database to create a simple user dataset by hand as I am not able to import any csv files.
You can check my dashboard to see where I created my dataset on "Linea LXP Wallet Stats" query. (https://dune.com/biksan/lxp-stats)
Original data from linea blockchain contains more than million rows. That might be the reason I could not get real meaningful cluster distribution after elbow plot.
I am looking for a real dataset enhance this project.



