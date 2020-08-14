var data ={
	"row": ["https://github.com/santosh8309/NewsBytes", "FANDFN489TGRNIRT489T"]
	
}
var list = data["row"]
var id = ''
for (var i=0; i<list.length; i++){
	td+='<td>'+list[i]+'</td>';
}
$('#table').append(td);