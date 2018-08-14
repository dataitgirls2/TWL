# install.packages("readxl")
# Loading
library("readxl")
# xls files
speed_dt<- read_excel("vc_dt_speed_seoul.xls")
speed_tot <- read_excel("vc_total_speed_seoul.xls")

for (i in 5:28){
print(t.test(speed_dt[i], speed_tot[i-1], alternative = "two.sided",
       mu=0, paired = F, var.equal = F, conf.level = 0.95))
print(i-4)
}

