
Student = function(name) {
    this.name = name || "no name set";
    this.email  = "no email set";
    this.address = new Address();
    this.scores = [];
    this.scores._dbCons = Score;
}

Student.prototype.summary = function() {
   var s = this.name + '\n';
   s += this.address.toString() + '\n';
   this.scores.forEach( function(score) { s += score.toString() + '\n'; } );
   return s;
}

Student.prototype.addScore = function(course, grade) {
   this.scores.push( new Score(course, grade) );
}

Student.prototype._transientFields = [ "gpa" , "_form" ];

Student.__proto__ = new ModelBase( "students" , Student );


