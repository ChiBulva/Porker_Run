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
              //alert( Results )
            }
            Query_Players(  );
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
            Query_Players(  );
        }
    });
}

function Get_Leaders( ) {
  $.ajax({
      type: 'POST',
      url: "/Get_Leaders",
      contentType: "application/json",
      //data: JSON.stringify( JSON_Data ),
      success: function (Results) {
        console.log( "Results!!!" )
        console.log( Results )
        console.log( "Results!!!" )
        $( "#Leaderboard_Area" ).empty();
        Count = 0
        for ( Player in Results[ "Players" ] ) {
          $( "#Leaderboard_Area" ).append( "<div class='g-width5 g-height5 g-FL'>#" + ( Count + 1 ) + "</div><div class='g-width30 g-height5 g-FL'>" + Results[ "Players" ][ Count ]['name'] + "</div><div class='g-width35 g-height5 g-FL'>" + Results[ "Players" ][ Count ]['hand'] + "</div><div class='g-width30 g-height5 g-FL'>" + Results[ "Players" ][ Count ]['hand_name'] + "</div>" );
          Count += 1
        }

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
          Count = 1
          for ( Player in Results[ "Players" ] ) {
            console.log( "Player" )
            HTML = "<div class='g-width100 g-height5 g-lightgray g-FL' >"

            HTML += "<div id='Player_User_" + Count + "' class='g-width45 g-height100 g-FL' onclick='Add_Name( this.innerHTML )'>" + Results[ "Players" ][ Player ][ "name" ] + "</div>"

            if( Results[ "Players" ][ Player ][ "paid" ] ) {
              // User has paid
              HTML += "<input type='checkbox' class='g-width5 g-height90 g-FL' onchange=\"Paid_Toggle(\'" + Results[ "Players" ][ Player ][ "name" ] + "\')\" checked />"

              if( Results[ "Players" ][ Player ][ "hand" ] == "" ){

                // Ask to add a users hand
                HTML += "<button id='User_" + Count + "' class='g-width48 g-height100 g-lightgreen g-text-white g-FR' onclick=\"Add_New_Hand(\'" + Results[ "Players" ][ Player ][ "name" ] + "\', 'User_" + Count + "' )\"/>Click to add Hand</button><div class='g-width48 g-height100 g-FR' style='display:none' id='Input_Container_User_" + Count + "'><input id='Input_User_" + Count + "' class='g-width85 g-height100 g-FL' placeholder=' Type Hand here ...' /><button class='g-width15 g-height100 g-green g-text-white g-FL' onclick=\"Add_Hand( 'User_" + Count + "' )\" >Add</button></div>"
              }
              else{
                // User should show up on leaderboard
                HTML += "<button id='User_" + Count + "' class='g-width48 g-yellow g-height100 g-FR' onclick=\"Add_New_Hand(\'" + Results[ "Players" ][ Player ][ "name" ] + "\', 'User_" + Count + "' )\"/>" + Results[ "Players" ][ Player ][ "hand" ] + "</button><div class='g-width48 g-height100 g-FR' style='display:none' id='Input_Container_User_" + Count + "'><input id='Input_User_" + Count + "' class='g-width85 g-height100 g-FL' placeholder=' Type Hand here ...' /><button class='g-width15 g-height100 g-green g-text-white g-FL' onclick=\"Add_Hand( 'User_" + Count + "' )\" >Add</button></div>"

              }
            }
            else{
              // User has not paid yet
              HTML += "<input type='checkbox' class='g-width5 g-height90 g-FL' onchange=\"Paid_Toggle(\'" + Results[ "Players" ][ Player ][ "name" ] + "\')\"/>"

              // Ask the user to pay
              HTML += "<div class='g-width48 g-height100 g-white g-text-red g-FR'>You'll need to pay</div>"
            }
            //HTML += "<div class='g-width33- g-height100 g-red g-FL'>" + Results[ "Players" ][ Player ][ "hand" ] + "</div>"
            //HTML += "<input class='g-width20 g-height100 g-FL'>" + Results[ "Players" ][ Player ][ "paid" ]
            //HTML += "<div class='g-width20 g-height100 g-FL'>" + Results[ "Players" ][ Player ][ "name" ] + "</div>"
            HTML += "</div>"
            //Results[ "Players" ][ Player ][ "paid" ]
            //Results[ "Players" ][ Player ][ "hand" ]

            console.log( Results[ "Players" ][ Player ][ "name" ] )


            $( "#Play_Info_Area" ).append( HTML );
            Count += 1
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
          Query_Players(  );
        }
    });
}

function Paid_Toggle( Player ) {
  Paid_Toggle_From_Server( Player );
}



function Query_Players(  ){
  Get_Players(  );
  Get_Leaders();
  //Assign_Player_HTML( Get_Players(  ) )
}

function Add_Hand_From_Server( Player, Hand ) {

    JSON_Data = {
      "Player_Name": Player,
      "Hand": Hand
    }

    $.ajax({
        type: 'POST',
        url: "/Add_Hand",
        contentType: "application/json",
        data: JSON.stringify( JSON_Data ),
        success: function (Results) {
          console.log( Results );
          Query_Players(  );
        }
    });
}

function Add_Hand( User_ID ) {
  Player = $("#Player_" + User_ID )[0].innerHTML
  Hand = $("#Input_" + User_ID )[0].value

  console.log(Player,Hand)

  Add_Hand_From_Server( Player, Hand );
}

function Add_New_Hand( Player_Name, DIV_ID ){
  console.log( $("#" + DIV_ID )[0] )
  console.log( $("#Input_" + DIV_ID )[0] )
  $("#Input_Container_" + DIV_ID ).show()
  $("#" + DIV_ID ).hide()
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
