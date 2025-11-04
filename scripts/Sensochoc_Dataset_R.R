# R script used to obtain the sensochoc data set from the sensehubr R package.

# install sensehubr
devtools::install_github("aswansyahputra/sensehubr")

library(sensehubr)

# store data in data.frame
df <- sensochoc


# write to csv file for use in Python
write.csv(df, file ="sensochoc_dataset.csv")


