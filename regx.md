// we are learning regx 


/**
 * Regx 
 * It is used to extract certain strings patterns from a corpous of a document
 * 
 * Alpha : A-Z a-z
 * Numberic : 0-9 
 * Special characters : !,-,#,$,
 * * any 
 * + one or more 
 * ? zero or 1 
 * d = digit 
 * [0-9] any thing between this 
 * [A-Z] any thing between this
 * ^ Start of the string 
 * $ end of the string
 * 
 * \d is only digit 
 * \D is non-digit 
 * \w is word character
 * \W is non word character
 * \s is space, tab, newline
 * \S is non-space, tab, newline 
 * 
 */




// RegExp(r'^[A-Za-z\d]+@[a-z\d]+[.][a-z]+$') this validates email 
// only special character RegExp(r"^[\D|W|S]+$")
// ony digit r"^\d{10}$"

void main(){

RegExp regx = RegExp(r"^[^A-Za-z0-9]+$");
print(regx.hasMatch("!!"));

}