import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl
import json

api_key = False
serviceurl = 'https://api.datayuge.com/v1/lookup/'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

data = '''
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/">
<soapenv:Header>
<com:AUFHeaderResponse xmlns:com="http://schemas.auf.com/integration/common">
<com:RequestId>C87892894718158925</com:RequestId>
</com:AUFHeaderResponse>
</soapenv:Header>
<soapenv:Body>
<ns2:GetCustomer360DetailsResponse xmlns:ns2="http://schemas.auf.com/integration/customer">
<ns2:TransactionStatus>
<com:ResponseCode xmlns:com="http://schemas.auf.com/integration/common">0</com:ResponseCode>
<com:ResponseMessage xmlns:com="http://schemas.auf.com/integration/common">Success</com:ResponseMessage>
<com:ExtendedErrorDetails xmlns:com="http://schemas.auf.com/integration/common"><com:messages><com:code>0</com:code>
</com:messages>
</com:ExtendedErrorDetails>
</ns2:TransactionStatus>
<ns2:CustomerResponse>
<ns2:CustomerBasicInquiry>
<com:CustomerId xmlns:com="http://schemas.auf.com/integration/common">24047514213</com:CustomerId>
<com:NationalIdentificationCode xmlns:com="http://schemas.auf.com/integration/common">8751</com:NationalIdentificationCode>
<com:CustomerName xmlns:com="http://schemas.auf.com/integration/common">
<com:Prefix>MR.</com:Prefix>
<com:FirstName>RAJ</com:FirstName>
<com:LastName>KU</com:LastName>
<com:ShortName>SK</com:ShortName>
<com:FormattedFullName>SUMAN##KU</com:FormattedFullName>
<com:FullName>SUMAN KU</com:FullName>
</com:CustomerName>
<com:CustomerFullName xmlns:com="http://schemas.auf.com/integration/common">SUMAN KU</com:CustomerFullName>
<com:OfficerID xmlns:com="http://schemas.auf.com/integration/common">First teller</com:OfficerID>
<com:CustomerAddress xmlns:com="http://schemas.auf.com/integration/common">
<com:Line1>wwww</com:Line1>
<com:City> NEW DELHI</com:City>
<com:State>DELHI</com:State>
<com:Country>India</com:Country>
<com:Zip>110001</com:Zip>
</com:CustomerAddress>
<com:BirthDateText xmlns:com="http://schemas.auf.com/integration/common">1976-06-03</com:BirthDateText>
<com:CategoryType xmlns:com="http://schemas.auf.com/integration/common">INDIVIDUAL - FULL KYC</com:CategoryType>
<com:Sex xmlns:com="http://schemas.auf.com/integration/common">F</com:Sex>
<com:IsImageAvailable xmlns:com="http://schemas.auf.com/integration/common">true</com:IsImageAvailable>
<com:IsSignatureAvailable xmlns:com="http://schemas.auf.com/integration/common">true</com:IsSignatureAvailable>
<com:CombWithdrawBal xmlns:com="http://schemas.auf.com/integration/common">0.0</com:CombWithdrawBal>
<com:AgeOfCustRel xmlns:com="http://schemas.auf.com/integration/common">2019-06-25</com:AgeOfCustRel>
<com:HomeBranch xmlns:com="http://schemas.auf.com/integration/common">2143</com:HomeBranch>
<com:MobileNumber xmlns:com="http://schemas.auf.com/integration/common">8903456566</com:MobileNumber>
<com:EmailAddress xmlns:com="http://schemas.auf.com/integration/common">gdhs76dsban45@gmail.com</com:EmailAddress>
<com:IcType xmlns:com="http://schemas.auf.com/integration/common">L</com:IcType>
<com:IcTypeDesc xmlns:com="http://schemas.auf.com/integration/common">Lead Number</com:IcTypeDesc>
<com:BankShortName xmlns:com="http://schemas.auf.com/integration/common">Palanpur_Abu National Highway</com:BankShortName>
<com:PAN xmlns:com="http://schemas.auf.com/integration/common">AAYYT6574L</com:PAN>
<com:CustomerType xmlns:com="http://schemas.auf.com/integration/common">100</com:CustomerType>
</ns2:CustomerBasicInquiry>
</ns2:CustomerResponse>
<ns2:AccountDetails><com:CustomerAccount xmlns:com="http://schemas.auf.com/integration/common"><com:ModuleCode>C</com:ModuleCode>
<com:ProductName>20234326-CURRENT ACCOUNT - RERA C</com:ProductName>
<com:AccountId>1921214323545891</com:AccountId>
<com:CASAAccountName> Raj Singhania</com:CASAAccountName>
<com:CurrencyCode>1</com:CurrencyCode>
<com:CurrencyShortName>INR</com:CurrencyShortName>
<com:CustomerRelationship>JAO</com:CustomerRelationship>
<com:BalanceBook>0.00</com:BalanceBook>
<com:UnclearFunds>0.00</com:UnclearFunds>
<com:Classification >NORMAL</com:Classification>
<com:Reason>UNBLOCKED</com:Reason>
<com:BillAmount>0.00</com:BillAmount>
<com:OriginalBalance>0.00</com:OriginalBalance>
<com:CurrentStatus>8</com:CurrentStatus>
<com:CurrentStatusDescription>ACCOUNT OPEN REGULAR</com:CurrentStatusDescription>
<com:AcyAmount>0.00</com:AcyAmount>
<com:AvailableBalance>0.00</com:AvailableBalance>
<com:LcyAmount>0.00</com:LcyAmount>
<com:TotalAcyAmount>0.00</com:TotalAcyAmount>
<com:TotalLcyAmount>0.00</com:TotalLcyAmount>
<com:BranchName>Palanpur _Abu National Highway</com:BranchName>
<com:ExternalAccountId>0</com:ExternalAccountId>
<com:FutureDatedAmount>0.00</com:FutureDatedAmount>
<com:SafeDepositBoxId>0</com:SafeDepositBoxId>
<com:DateAccountOpen>2019-06-25</com:DateAccountOpen>
<com:DateRelation>2019-06-25</com:DateRelation>
<com:MonthsSinceActive>1</com:MonthsSinceActive>
<com:BalUncollectedPrinc>0.00</com:BalUncollectedPrinc>
<com:BalUncollectedInt>0.00</com:BalUncollectedInt>
<com:TotalBalUncollecPrinc>0.00</com:TotalBalUncollecPrinc>
<com:TotalBalUncollecInt>0.00</com:TotalBalUncollecInt>
<com:TotalBalBook>0.00</com:TotalBalBook>
<com:DateValue>2019-06-25</com:DateValue>
<com:BalPrincipal>0</com:BalPrincipal>
<com:IntRate>0</com:IntRate>
<com:LienAmount>0</com:LienAmount>
<com:InstallmentAmount>0</com:InstallmentAmount>
<com:OtherArrear>0</com:OtherArrear>
<com:BalCombinedAcy>0.0</com:BalCombinedAcy>
<com:BalCombinedLcy>0.0</com:BalCombinedLcy>
<com:BranchCode>2143</com:BranchCode>
<com:IsTDLinkage>N</com:IsTDLinkage>
<com:HoldAmount>0</com:HoldAmount>
<com:ODLimitSactioned>0</com:ODLimitSactioned>
<com:ODLimitUtilized>0</com:ODLimitUtilized>
<com:CASARelationshipDetails>
<com:CustomerId>24047514</com:CustomerId>
<com:JointHolderName>Raj Singhania</com:JointHolderName>
<com:MobileNo>7021547608</com:MobileNo>
<com:Relationship>JAF</com:Relationship>
</com:CASARelationshipDetails>
<com:CASARelationshipDetails>
<com:CustomerId>24047513421</com:CustomerId>
<com:Emailid>gdhs45@gmail.com</com:Emailid>
<com:JointHolderName>SUMAN KU</com:JointHolderName>
<com:Relationship>JAO</com:Relationship>
</com:CASARelationshipDetails>
<com:AmtGoal>0</com:AmtGoal>
<com:ProductCode>20236</com:ProductCode>
<com:Tenure>0 Months 0 Days 0 Years</com:Tenure>
</com:CustomerAccount>
<com:IsCustomerSchemeAvailable xmlns:com="http://schemas.auf.com/integration/common">false</com:IsCustomerSchemeAvailable>
</ns2:AccountDetails>
</ns2:GetCustomer360DetailsResponse>
</soapenv:Body>
</soapenv:Envelope> 
'''

tree = ET.fromstring(data)
ns = {'com':'http://schemas.auf.com/integration/common'}

for element in tree.findall('.//com:MobileNumber', ns):
    number = element.text

print(number)

url = serviceurl + number
print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read().decode()
try:
   js = json.loads(data)
except:
    js = None
print(json.dumps(js, indent=4))