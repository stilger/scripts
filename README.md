# Misc Scripts

#### mwgrinmanual.py - Used for manual download and upload of slate files from [MWGrinPool](https://www.mwgrinpool.com)
    * Requirements: python3 and requests module
    * Run: mwgrinmanaul.py -h for help:
    
          --pool_user POOL_USER Username on MWGrinPool
          
          --pool_pass POOL_PASS Password on MWGrinPool
          
          --file_name FILE_NAME File Name
          
          --get_unsigned        Get MWGrinPool Unsigned Slate
          
          --send_signed         Send MWGrinPool Signed Slate

    * Run: mwgrinmanaul.py without switched to get current balance it will prompt for MWgrinPool login and password. 
    * Run: mwgrinmanaul.py --get_unsigned to download unisgned slate file from MWGrinPool
    * Run: mwgrinmanaul.py --send_signed to upload signed slate file to MWGrinPool

    Steps:
    * mwgrinmanaul.py --get_unsigned to save file
    * Upload/Transfer file to Exchange or wallet. 
    * Sign file 
    * Download signed file to new name
    * mwgrinmanaul.py --send_signed using downloaded file
