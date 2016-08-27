# Relevant stuff in the database

# Identifying people

In table `academic`, each row identifies a person.  `academic_id` is
an integer which is used to identify this person in the database.
This is the number we should use internally for a person.
`family_name`, `given_name` and `other_names` contain the name of the
person.  They could involve non-ASCII UTF-8 (?) characters.

To further help identify a person, MGP gives their degree, year and
school.  Table `degree` has columns:

- `degree_id` is an ID number for this degree

- `academic_id` is the ID number of the person to whom the degree is
  awarded

- `year` is the year in which the degree was awarded

- `thesis` is the thesis title which could be useful maybe

- `degree_type` is a string describing the kind of degree, usually
  `"Ph.D."`.

To identify the school, look at table `degree_grant`.  Column `degree`
is the ID of a degree and `school` is the ID of a school.  In theory
there could be two columns with the same `degree`, I guess if a degree
is jointly awarded by two or more schools?

Schools are listed in table `school`.  `school_id` is the ID number,
`school_name` is the school name, and `country` is an ID number of the
country where the school is located.  Country ID is mapped to country
name via the table `country`.

# Identifying relationships

Relationships are mostly in the table `advises`.  The columns
`advisor` and `advisee` are ID numbers of the corresponding people.
`advice_type` says something about the advisor's role; usually it is
just `"Advisor"` but could also be `"Advisor 1", "Co-Advisor"`, etc.
We probably don't care about this.  `degree` is the numeric degree ID,
see above.

# Size

As of this writing there are 201330 rows in `academic` and 214319 rows
in `advises`.
