
# Introduction

Linea is a scalable Layer 2 blockchain network built on Ethereum, designed to enhance transaction speed and lower costs while maintaining Ethereum's robust security. 
Linea is planning an airdrop campaign to award their users. They are distributing Linea Voyage XP (LXP) tokens to user wallets, which is an ERC-20 token you can receive for participating in the Linea Voyage — a series of community events where you use various elements of the Linea ecosystem to help us test, grow, and build.
In this project, I segmented users using their activiy on the blockchain, including LXP points.

# Background
Using the query below, dataset is taken from Dune Analytics, which is a platform that provides users with tools to create their own blockchain data-fed charts and dashboards.
Original data contains more than million rows. As I was not able to import as a csv file, I took only a portion of it manually.

```sql
SELECT *
FROM dune.dune.result_linea_lxp_holder_stats;
```

![image](https://github.com/user-attachments/assets/910a2b05-2b2a-4149-b66c-9060c2bcae85)

## Tools
- **Python:** My primary programming language for data analysis, user segmentation, modeling and visualisation.
- **Pycharm:** My primary integrated development environment (IDE) used for programming in Python. 
- **Dune Analytics:** The platform enabling queries to extract blockchain user data and creating dashboards.

## Dataset 

- **Wallet:** Unique wallet of each user
- **Current LXP:** LXP distributed to each wallet
- **Num Quests:** Number of quests completed
- **On Farcaster:** Indicates if the user has a Farcaster account
- **FID:** Farcaster user ID
- **Fname:** Farcaster nickname
- **Connected Wallets:** Other wallet addresses connected to main wallet
- **Num Followers:** Number of followers the user has
- **Num Onchain Txns:** Count of on-chain transactions on Linea
- **Days Old Onchain:** Active days on Linea
- **NFT Volume(USD):** NFT trade volume on Linea in USD
- **DEX Volume(USD):** Decentralized exchange trade volume on Linea in USD
- **Contracts Deployed:** Number of contracts deployed on Linea
- **Time Contracts Called:** Number of times contacts were called on Linea

# Analysis

For user segmentation, I selected the variables as "current lxp","dex_volume_usd","num_onchain_txns","days_old_onchain, which I considered as the most important statistics showing user activity on a blockchain.
Scaled these variables between 0 and 1 for k-means clustering.
Elbow plot specified the optimum number of clusters as k=7.

![elbow_plot](https://github.com/user-attachments/assets/a1dc2ea7-e894-4800-81a3-a311ef911150)

For k=7, there were 3 clusters with only 1 user so I redefined cluster number as k=5.

For k=5, there were 2 clusters with only 1 user. Examining variables, I placed 2 clusters to the closest cluster and obtained 3 clusters as most active, active and normal users.

For final 3 clusters, cluster-wise variables are shown below:

![Fotoram io](https://github.com/user-attachments/assets/bf711790-fc08-4ca1-9df1-09d289406da4)

## Creating a Dashboard for Linea Blockchain

In addition to user segmentation, I created a dashboard on Dune to observe crucial user statistics on Linea blockchain.
This is not mandatory for this particular project. However, I wanted to show some key statistics for LXP distribution.

### Linea Wallet LXP Stats ###

I used a simple query to investigate how LXP distributed among wallets. It is shown as "LXP Stats" on the dashboard.

```sql
SELECT
    lxp_range,
    COUNT(DISTINCT wallet) AS wallet_count,
    SUM(current_lxp) AS total_lxp
FROM (
    SELECT 
        wallet,
        current_lxp,
        CASE
            WHEN current_lxp < 1000 THEN '<1000'
            WHEN current_lxp BETWEEN 1000 AND 1999 THEN '1000-1999'
            WHEN current_lxp BETWEEN 2000 AND 2999 THEN '2000-2999'
            WHEN current_lxp BETWEEN 3000 AND 3999 THEN '3000-3999'
            WHEN current_lxp BETWEEN 4000 AND 4999 THEN '4000-4999'
            WHEN current_lxp BETWEEN 5000 AND 5999 THEN '5000-5999'
            WHEN current_lxp BETWEEN 6000 AND 6999 THEN '6000-6999'
            WHEN current_lxp BETWEEN 7000 AND 7999 THEN '7000-7999'
            WHEN current_lxp BETWEEN 8000 AND 8999 THEN '8000-8999'
            WHEN current_lxp BETWEEN 9000 AND 9999 THEN '9000-9999'
            WHEN current_lxp >= 10000 THEN '10000>'
        END AS lxp_range
    FROM dune.dune.result_linea_lxp_holder_stats
) AS lxp_data
GROUP BY lxp_range
ORDER BY wallet_count;
```
![Linea Dashboard](https://github.com/user-attachments/assets/f3dd41df-1eff-465b-8c2d-d6d4f5475c6c)

## Key Observations

- **Current LXP:** Active users seems to have a bit more LXP points than most active users, which may be unexpected. We can observe that current lxp is not the key variable to segment users for their activity.
- **Dex Volume(USD):** The key variable discriminates most active users among others.
- **Days on Onchain:** Most active users have >1600 days onchain activity, active users have >1200 days and other users have >800 days.
- **Num Onchain Txns:** Most active users have >12000 txsn, active users have >6000 and other users have around 2000 txns. 

For a fair airdrop distribution, these user segments may be simply used. While more active users receive more tokens, less active users receive less.


# Conclusion

In this project, I used k-means clustering algorithm for user segmentation, using key indicators showing wallet activity on a blockchain. 
For user segmentation, variable selection may differentiate upon business decision. In this case, I selected the variables according to my experiences as a blockchain user.

I learned how to use Dune Analytics with queries to create a blockchain user dataset.
You can check my dashboard to see where I created my dataset on "Linea LXP Wallet Stats" query. (https://dune.com/biksan/lxp-stats)

Original data from linea blockchain contains more than million rows. However, as I was not able to import original data as csv, I collected a portion of the original data.
For better results in case of clustering, an original dataset may be helpful.



