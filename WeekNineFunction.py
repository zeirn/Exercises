
# My class functions where I get the loan amount, the number of years, and the interest rate.
class Mortgage(object):
    # Putting all inputs not involving points in first class.
    def __init__(self, loan_amount, fixed_APR, years):
        """ My loan amount and interest rate """
        self.loan_amount = loan_amount
        self.fixed_APR = fixed_APR
        self.years = years
        self.pay_monthly = None
        self.pay_total = None

    def get_loan_amount(self):
        return self.loan_amount

    def get_fixed_APR(self):
        return self.fixed_APR

    def get_years(self):
        return self.years

    # Calculate interest, nom, and monthly payment. Use monthly payment to calculate total payment.
    def set_pay_monthly(self):
        """ This method gets the total payment """
        interest = self.fixed_APR / 12
        nom = self.years * 12
        monthly_payment = self.loan_amount * (interest * ((1 + interest) ** nom) / (((1 + interest) ** nom) - 1))
        yearly_payment = monthly_payment * 12
        total_payment = self.years * yearly_payment
        return total_payment

# My subset class function where I add points to mortgage.
class Points_Mortgage(Mortgage):

    def __init__(self, loan_amount, fixed_APR, years, points, APR_points):
        Mortgage.__init__(self, loan_amount, fixed_APR, years)
        self.points = points
        self.APR_points = APR_points
        self.include_points = None

    def get_points(self):
        return self.points

    def get_APR_points(self):
        return self.APR_points

    # Same thing done in 'set_pay_monthly', except I replace fixed_APR w/ APR_points and add initial payment to total
    def set_include_points(self):
        """ This method includes points in the equation """
        interest = self.APR_points / 12
        nom = self.years * 12
        monthly_payment = self.loan_amount * (interest * ((1 + interest) ** nom) / (((1 + interest) ** nom) - 1))
        yearly_payment = monthly_payment * 12
        total_payment = self.years * yearly_payment
        initial_payment = (self.points / 100) * self.loan_amount
        fixed_total_payment = total_payment + initial_payment
        return fixed_total_payment
