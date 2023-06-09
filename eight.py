from re import split
def main(s):
    split_list = list(filter(None, split(" |def|@|[[]|[]]|<=|\n", s)))
    print(split_list)

print(main('||<% declare @"dila" <- { 5240 7869 -875}. %>. <% declare @"eddi" <-{ -2506 -3261 -3782 2201 }. %>. <% declare @"errete_834"<- { 2430 -238-6037 5737}. %>. <% declare @"inor_461" <- { -8065 -9620}. %>. ||'))