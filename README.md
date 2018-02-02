# CS-GY-9223-G-BIG-DATA-ANALYTICS-Fall-2017

## Command lines:
- [Set up the SSH tunnel to HPC](https://wikis.nyu.edu/pages/viewpage.action?pageId=84607390)

  After setting up, use `ssh hpctunnel` and `ssh dumbo` to access the HPC DUMBO clusters.
  
  
- Interact with HDFS
  * Copy the input file to HDFS: `hadoop fs -copyFromLocal sherlock.txt`


- Fetch files from HPC:
  `scp xg626@dumbo.hpc.nyu.edu:/home/xg626/xxx.csv ./GoogleDrive/`
  
  ```
  Tonys-Mac:Downloads dc$ scp -v NYPD_Complaint_Data_Current_YTD.csv xg626@dumbo.hpc.nyu.edu:/home/xg626/nycdata/
  Executing: program /usr/bin/ssh host dumbo.hpc.nyu.edu, user xg626, command scp -v -t /home/xg626/nycdata/
  OpenSSH_6.2p2, OSSLShim 0.9.8r 8 Dec 2011
  debug1: Reading configuration data /Users/dc/.ssh/config
  debug1: Reading configuration data /etc/ssh_config
  debug1: /etc/ssh_config line 20: Applying options for *
  debug1: Connecting to dumbo.hpc.nyu.edu [128.122.215.52] port 22.
  debug1: connect to address 128.122.215.52 port 22: Operation timed out
  debug1: Connecting to dumbo.hpc.nyu.edu [128.122.215.51] port 22.
  debug1: connect to address 128.122.215.51 port 22: Operation timed out
  ssh: connect to host dumbo.hpc.nyu.edu port 22: Operation timed out
  lost connection
  Tonys-Mac:Downloads dc$ scp -v NYPD_Complaint_Data_Current_YTD.csv dumbo:/home/xg626/nycdata/
  Executing: program /usr/bin/ssh host dumbo, user (unspecified), command scp -v -t /home/xg626/nycdata/
  OpenSSH_6.2p2, OSSLShim 0.9.8r 8 Dec 2011
  debug1: Reading configuration data /Users/dc/.ssh/config
  debug1: /Users/dc/.ssh/config line 13: Applying options for dumbo
  debug1: Reading configuration data /etc/ssh_config
  debug1: /etc/ssh_config line 20: Applying options for *
  debug1: Connecting to localhost [::1] port 8025.
  debug1: Connection established.
  debug1: identity file /Users/dc/.ssh/id_rsa type -1
  debug1: identity file /Users/dc/.ssh/id_rsa-cert type -1
  debug1: identity file /Users/dc/.ssh/id_dsa type -1
  debug1: identity file /Users/dc/.ssh/id_dsa-cert type -1
  debug1: Enabling compatibility mode for protocol 2.0
  debug1: Local version string SSH-2.0-OpenSSH_6.2
  debug1: Remote protocol version 2.0, remote software version OpenSSH_5.3
  debug1: match: OpenSSH_5.3 pat OpenSSH_5*
  debug1: SSH2_MSG_KEXINIT sent
  debug1: SSH2_MSG_KEXINIT received
  debug1: kex: server->client aes128-ctr hmac-md5 none
  debug1: kex: client->server aes128-ctr hmac-md5 none
  debug1: SSH2_MSG_KEX_DH_GEX_REQUEST(1024<1024<8192) sent
  debug1: expecting SSH2_MSG_KEX_DH_GEX_GROUP
  debug1: SSH2_MSG_KEX_DH_GEX_INIT sent
  debug1: expecting SSH2_MSG_KEX_DH_GEX_REPLY
  debug1: Server host key: RSA ea:0b:ec:4a:5b:98:8b:a3:1f:36:a9:44:cc:cb:92:78
  debug1: Host '[localhost]:8025' is known and matches the RSA host key.
  debug1: Found key in /Users/dc/.ssh/known_hosts:20
  debug1: ssh_rsa_verify: signature correct
  debug1: SSH2_MSG_NEWKEYS sent
  debug1: expecting SSH2_MSG_NEWKEYS
  debug1: SSH2_MSG_NEWKEYS received
  debug1: SSH2_MSG_SERVICE_REQUEST sent
  debug1: SSH2_MSG_SERVICE_ACCEPT received
  debug1: Authentications that can continue: publickey,gssapi-keyex,gssapi-with-mic,password,keyboard-interactive,hostbased
  debug1: Next authentication method: publickey
  debug1: Trying private key: /Users/dc/.ssh/id_rsa
  debug1: Trying private key: /Users/dc/.ssh/id_dsa
  debug1: Next authentication method: keyboard-interactive
  Password: 
  debug1: Authentication succeeded (keyboard-interactive).
  Authenticated to localhost ([::1]:8025).
  debug1: channel 0: new [client-session]
  debug1: Requesting no-more-sessions@openssh.com
  debug1: Entering interactive session.
  debug1: Sending environment.
  debug1: Sending env LANG = en_US.UTF-8
  debug1: Sending command: scp -v -t /home/xg626/nycdata/
  Sending file modes: C0644 121572958 NYPD_Complaint_Data_Current_YTD.csv
  Sink: C0644 121572958 NYPD_Complaint_Data_Current_YTD.csv
  NYPD_Complaint_Data_Current_YTD.csv           100%  116MB 537.2KB/s   03:41    
  debug1: client_input_channel_req: channel 0 rtype exit-status reply 0
  debug1: channel 0: free: client-session, nchannels 1
  debug1: fd 0 clearing O_NONBLOCK
  debug1: fd 1 clearing O_NONBLOCK
  Transferred: sent 121812880, received 36192 bytes, in 224.2 seconds
  Bytes per second: sent 543262.2, received 161.4
  debug1: Exit status 0
  ```
  See [Moving files between your workstation and HDFS](https://wikis.nyu.edu/display/NYUHPC/Clusters+-+Dumbo#Clusters-Dumbo-StorageonDumbo).
