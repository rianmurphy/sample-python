Course = function(name) {
    this.name = name || "name not set";
}

Course.prototype.toString = function() { return 'Course ' + this.name; }

Course.__proto__ = new ModelBase( "courses" , Course );

