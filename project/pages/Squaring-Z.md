title: Squaring Z 
date: 2019-01-08
abstract: Proving the square of a standard normal is chi-square with 1 degree of freedom.
topic: Statistics
color: "F0433A"
unlisted: 0

If $Z \sim N(0,1)$, then $Z^2  \sim \chi_{(1)}^2$

<b>Proof:</b>   $$M_{Z^2}(t)=E(e^{tZ^2}) = \int_{-\infty}^{\infty} e^{tZ^2}\frac{1}{\sqrt{2\pi}}e^{\frac{1}{2}Z^2}dz$$
$$ \Rightarrow \int_{-\infty}^{\infty} \frac{1}{\sqrt{2\pi}}e^{\frac{1}{2\frac{1}{1-2t}}Z^2}dz = \frac{1}{\sqrt{1-2t}}\int_{-\infty}^{\infty} \frac{1}{\sqrt{2\pi}\frac{1}{\sqrt{1-2t}}}e^{\frac{1}{2\frac{1}{1-2t}}Z^2}dz = \frac{1}{\sqrt{1-2t}}$$

Note that what's inside of the integral is simply $N(0,\sqrt{1-2t})$ which integrates to 1. 

Hence, $Z^2 \sim \chi_{(1)}^2$ noting $\frac{1}{1-2t}$ is the moment generating function for $\chi_{(1)}^2$ by definition.   




