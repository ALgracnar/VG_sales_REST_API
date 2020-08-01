from flask_restplus import reqparse

parse_arguments = reqparse.RequestParser()  # Parsing for regular queries

parse_arguments.add_argument('Name', type=str, required=False, default=None,
                             help='Gives detailes of of particular Video game(other fields are irrelevant)')
parse_arguments.add_argument('Platform', type=str, required=False, default=None,
                             help='Gives a list of Video games filterd by Platform: Wii, PS2....')
parse_arguments.add_argument('Year', type=str, required=False, default=None,
                             help='Gives the list of Video games published in particular Year')
parse_arguments.add_argument('Genre', type=str, required=False, default=None,
                             help='Gives a list of Video games filterd by Genre: Sports, Racing....')
parse_arguments.add_argument('Publisher', type=str, required=False, default=None,
                             help='Gives a list of Video games filterd by publisher: Nintendo, Microsoft Game Studios...')

parse_arguments_2 = reqparse.RequestParser()  # Parsing for querry greather than, less than

parse_arguments_2.add_argument('Column_to_filter', type=str, required=False,
                               choices=['Year', 'NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales'],
                               default=None,
                               help='Chose the column to filter Greater_than, Less_than.. Works if all 3 fields are specified!!')
parse_arguments_2.add_argument('Greater_than', type=float, required=False, default=None,
                               help='Chose the greater than argument. For Year-> 2000.For EU_Sales-> 1.6.... ')
parse_arguments_2.add_argument('Less_than', type=float, required=False, default=None,
                               help='Chose the less than argument. For Year-> 2006.For EU_Sales-> 5.2.... ')

parse_arguments_3 = reqparse.RequestParser()  # Parsing for sorting

parse_arguments_3.add_argument('Sort', type=str, required=False,
                               choices=['Rank', 'Name', 'Platform', 'Year', 'Genre', 'Publisher', 'NA_Sales',
                                        'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales'], default=None,
                               help='Specify sorting column')
parse_arguments_3.add_argument('Descending', type=str, required=False, choices=['True'], default=None,
                               help='Should sorting be descending?. Use only if Sort is specified!!')
