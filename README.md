# Software Now Assignment-02
<table width = "20%">
  <tr>
    <td> 
        
**Team Members** 

|Student Name (Github Id)|Student # |  
|--|--|
|Bipin Maharjan (geeksgod)  | s384170 |
|Muhammad Waqas Iqbal (LetwaqasKnow)| s376399
|Susan Shrestha (Susan0901)|s386445
|Bikash Sunuwar (sbikash196)|s385661|   

</td> 
    <td>
      <img src="https://digitalcollections.cdu.edu.au/assets/pic/2934" width="50%"/>
    </td>
    
  </tr>
</table>




**Project Folder Structure**

├── Encryption_files                 &emsp;&emsp;      ->  _Contains input and output of encryption algorithm (Question 1)_  
    │   ├── decrypted_text.txt          &emsp;&emsp; ->  _The decrypted text is written to this file_  
    │   ├── encrypted_text.txt          &emsp;&emsp;  -> _The encrypted text is written to this file_  
    │   └── key_file.txt                &emsp;&emsp;  -> _The key generated during encryption is written here_  
    │   └── raw_text.txt                &emsp;&emsp; ->  _The original text is present here_  
├── Helper                              &emsp;&emsp; -> _Contains helper functions for validation_  
    │   ├── helper.py                   &emsp;&emsp; -> _Contains input validation logic_  
├── Temperature_data                    &emsp;&emsp; ->  _Contains data of temperature from different stations_  
├── Temperature_output_files                   &emsp;&emsp;  -> _Contains input and output of temperature calculation (Question 2)_  
    │   ├── average_temp.txt            &emsp;&emsp; -> _average temperature for the seasons is written in this file_  
    │   ├── largest_temp_range_station.txt      &emsp;&emsp; -> _Station with largest temperature range  is written in this file_  
    │   └── warmest_and_coolest_station.txt     &emsp;&emsp; -> _Station with warmest and coolest temperature is written in this file_  
├── Question1_Encryption_Decryption.py  &emsp;&emsp; ->  _Contains solution for Question1_  
├── Question2_TemperatureAverage.py &emsp;&emsp;  -> _Contains solution for Question2_  
├── Question3_turtle_tree.py &emsp;&emsp; ->  _Contains solution for Question3_  

## Running the code
**Change the directory to the project folder**
```console
cd "Path to the project folder"
```

**To view the solution for question 1**
```console
python Question1_Encryption_Decryption.py
```
Running the command will generate a encrypted text, key and decrypted text file for the text in raw_text.txt

**To view solution for question 2**

```console
python Question2_TemperatureAverage.py
```
Running the command will generate the average temp for each season, station with highest temp range, warmest and coolest station


**To view solution for question 3**
```console
python  Question3_turtle_tree.py
```

Running the command will ask for input and create a recursive tree based on the input with the help of the turtle





