<?php 

// Add message
echo "<h1 style='color:red; text-decoration: underline;' align='center'>#CS378 Git Gud</h1>";

// Add syle
echo "<style>
          table {
 	      font-family: arial, sans-serif;
              border-collapse: collapse;
              width: 50%;
          }
          td, th {
              border: 1px solid #dddddd;
              text-align: left;
              padding: 8px;
          }  
          tr:nth-child(even) {
              background-color: #dddddd;
          }
       </style>";   

echo "<h3>Grabbed:</h3>"; 

$username = $_POST['email'];
$password = $_POST['pass'];

echo "<table>
          <tr> 
 	      <th>Username</th>
 	      <th>Password</th>
      </table>";

?>
