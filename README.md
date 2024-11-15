Linea is a scalable Layer 2 blockchain network built on Ethereum, designed to enhance transaction speed and lower costs while maintaining Ethereum's robust security. 
Linea is planning an airdrop campaign to award their users. They are distributing Linea Voyage XP (LXP) tokens to user wallets, which is an ERC-20 token you can receive for participating in the Linea Voyage — a series of community events where you use various elements of the Linea ecosystem to help us test, grow, and build.
In this project, I segmented users using their activiy on the blockchain, including LXP points.

![image](https://github.com/user-attachments/assets/612b3f8f-47a7-42a6-962b-a0a3160f79b6)

For customer segmentation, I selected the variables as "current lxp","dex_volume_usd","num_onchain_txns","days_old_onchain.
Scaled these variables between 0 and 1 for k-means clustering.
Elbow plot specified the optimum number of clusters as k=7.
![elbow_plot](https://github.com/user-attachments/assets/a1dc2ea7-e894-4800-81a3-a311ef911150)

For k=7, there were 3 clusters with 1 user so I redefined cluster number as k=5.

For k=5, there were 2 clusters with 1. Examining variables, I placed 2 clusters to the closest cluster and obtained 3 clusters as most active, active and normal users.

![Fotoram io](https://github.com/user-attachments/assets/bf711790-fc08-4ca1-9df1-09d289406da4)


Comments:
I used sql queries in Dune Analytics database to create a simple user dataset by hand as I am not able to import any csv files.
You can check my dashboard to see where I created my dataset on "Linea LXP Wallet Stats" query. (https://dune.com/biksan/lxp-stats)
Original data from linea blockchain contains more than million rows. For better results, bigger datasets may be helpful.
I am looking for a real dataset enhance this project.

![Linea Dashboard](https://github.com/user-attachments/assets/f3dd41df-1eff-465b-8c2d-d6d4f5475c6c)

