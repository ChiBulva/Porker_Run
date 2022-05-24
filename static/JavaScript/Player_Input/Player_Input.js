function Add_Player(  ){
  Player = $( "#Player_Name" )[0].value
  Paid = $( "#Player_Paid" )[0].checked

  //console.log( $( "#Player_Name" )[0].value )
  if( Player == "" ){
    alert( "Player name cannot be empty" )
  }
  else {
      Add_New_Player_From_Server( Player, Paid )
  }
}

function Remove_Player(  ){
  Player = $( "#Player_Name" )[0].value
  //console.log( $( "#Player_Name" )[0].value )
  if( Player == "" ){
    alert( "Player name cannot be empty" )
  }
  else {
      Remove_Player_From_Server( Player )
  }
}

//function Get_Report_Names_From_Server( Test_JS ) {
function Add_New_Player_From_Server( Player, Paid ) {
    JSON_Data = {
      "Player_Name": Player,
      "Paid": Paid
    }

    Report_Names = $.ajax({
        type: 'POST',
        url: "/Add_Player",
        contentType: "application/json",
        data: JSON.stringify( JSON_Data ),
        success: function (Results) {
            console.log( Results )
            if( Results == "Player_Exists!!!" ){
                alert( "Player Exists!!!" )
            }
            else if( Results == "Error!!!" ){
                alert( "Error when adding player!!!" )

            }
            else{
              alert( Results )
            }
            Get_Players(  );
        }
    });
}

//function Get_Report_Names_From_Server( Test_JS ) {
function Remove_Player_From_Server( Player ) {

    JSON_Data = {
      "Player_Name": Player
    }

    Report_Names = $.ajax({
        type: 'POST',
        url: "/Remove_Player",
        contentType: "application/json",
        data: JSON.stringify( JSON_Data ),
        success: function (Results) {
            console.log( Results )
            if( Results == "Player_Exists!!!" ){
                alert( "Player Exists!!!" )
            }
            else if( Results == "Error!!!" ){
                alert( "Error when adding player!!!" )

            }
            else{
              alert( Results )
            }
            Get_Players(  );
        }
    });
}

function Get_Players(  ) {

  Report_Names = $.ajax({
      type: 'POST',
      url: "/Get_Players",
      contentType: "application/json",
      //data: JSON.stringify( JSON_Data ),
      success: function (Results) {
          $( "#Play_Info_Area" ).empty();
          for ( Player in Results[ "Players" ] ) {
            console.log( "Player" )
            HTML = "<div class='g-width100 g-height5 g-blue g-FL' >"

            HTML += "<div class='g-width45 g-height100 g-red g-FL' onclick='Add_Name( this.innerHTML )'>" + Results[ "Players" ][ Player ][ "name" ] + "</div>"

            if( Results[ "Players" ][ Player ][ "paid" ] ) {
              // User has paid
              HTML += "<input type='checkbox' class='g-width5 g-height90 g-FL' onchange=\"Paid_Toggle(\'" + Results[ "Players" ][ Player ][ "name" ] + "\')\" checked />"

              if( Results[ "Players" ][ Player ][ "hand" ] == "" ){

                // Ask to add a users hand
                HTML += "<button class='g-width48 g-height100 g-blue g-FR' onclick=\"Add_Hand(\'" + Results[ "Players" ][ Player ][ "name" ] + "\')\"/>Click to add Hand</button>"
              }
              else{

                // User should show up on leaderboard
                HTML += "<button class='g-width48 g-yellow g-height100 g-FR'>" + Results[ "Players" ][ Player ][ "hand" ] + "</button>"
              }
            }
            else{
              // User has not paid yet
              HTML += "<input type='checkbox' class='g-width5 g-height90 g-FL' onchange=\"Paid_Toggle(\'" + Results[ "Players" ][ Player ][ "name" ] + "\')\"/>"

              // Ask the user to pay
              HTML += "<button class='g-width48 g-height100 g-white g-text-red g-FR'>You'll need to pay</button>"
            }
            //HTML += "<div class='g-width33- g-height100 g-red g-FL'>" + Results[ "Players" ][ Player ][ "hand" ] + "</div>"
            //HTML += "<input class='g-width20 g-height100 g-FL'>" + Results[ "Players" ][ Player ][ "paid" ]
            //HTML += "<div class='g-width20 g-height100 g-FL'>" + Results[ "Players" ][ Player ][ "name" ] + "</div>"
            HTML += "</div>"
            //Results[ "Players" ][ Player ][ "paid" ]
            //Results[ "Players" ][ Player ][ "hand" ]

            console.log( Results[ "Players" ][ Player ][ "name" ] )


            $( "#Play_Info_Area" ).append( HTML );
          }
      }
  });
}

function Paid_Toggle_From_Server( Player ) {
    console.log( "--> " + Player )

    JSON_Data = {
      "Player_Name": Player
    }

    $.ajax({
        type: 'POST',
        url: "/Paid_Toggle",
        contentType: "application/json",
        data: JSON.stringify( JSON_Data ),
        success: function (Results) {
          console.log( Results );
          Get_Players(  );
        }
    });
}

function Paid_Toggle( Player ) {
  Paid_Toggle_From_Server( Player );
}



function Query_Players(  ){
  Get_Players(  );
  //Assign_Player_HTML( Get_Players(  ) )
}

function Add_Hand_From_Server( Player ) {

    JSON_Data = {
      "Player_Name": Player
    }

    $.ajax({
        type: 'POST',
        url: "/Add_Hand",
        contentType: "application/json",
        data: JSON.stringify( JSON_Data ),
        success: function (Results) {
          console.log( Results );
        }
    });
}

function Add_Hand( Player ) {
    Add_Hand_From_Server( Player );
}

function Add_Name( Player_Name ) {
    console.log(Player_Name);
    $( "#Player_Name" )[0].value = Player_Name;
}

// ************************************************************
// ** Runs on load of the page

$(document).ready(function () {
  Query_Players(  );
});

// **
// ************************************************************
