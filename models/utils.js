
// this contains objects that aren't 1st class
// (don't have their own collection in the db)


Address = function(s,c,st,pc) {
   this.street = s||"";
   this.city = c||"asd";
   this.state = st||"";
   this.postalCode = pc||"";
}
Address.prototype.toString = function() {
   return this.street + '\n' + this.city + ', ' +
     this.state + ' ' + this.postalCode;
}

// grade for a class
Score = function(course,grd) {
   this.for_course = course; // course
   this.grade = grd || 0.0;
}
Score.prototype.toString = function() {
   return this.for_course.toString() + ': ' + this.grade;
}
Score.prototype.passed = function() { return this.grade >= 2.0; }

