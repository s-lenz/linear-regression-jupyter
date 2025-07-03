# Load libraries
library(ggplot2)

# Get args
args <- commandArgs(trailingOnly = TRUE)

filename <- args[1]
x <- args[2]
y <- args[3]

# Describe data
df <- read.csv(filename)

# Fit model to data
model <- lm(as.formula(paste(y, "~", x)), data = df)
slope <- coef(model)[2]
intercept <- coef(model)[1]
r <- cor(df[[x]], df[[y]])
pred <- predict(model)
mse <- mean((df[[y]] - pred)^2)

# Plot the data
ggplot(df, aes_string(x = x, y = y)) +
  geom_point() +
  geom_smooth(method = "lm", se = FALSE, color = "red") +
  annotate("text", x = 1.5, y = max(df$y) - 0.5,
           label = paste("y =", round(slope, 2), "x +", round(intercept, 2),
                         "\nr =", round(r, 2), "\nMSE =", round(mse, 2)),
           size = 4) +
  labs(title = "Linear Fit",
       x = "x", y = "y") +
  theme_minimal()
ggsave("regression_plot_r.png")


