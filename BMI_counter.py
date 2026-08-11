print("Calculate your BMI")
weight=float(input("Enter your weight in KG:"))
height_feet=float(input("Enter your height feet:"))
height_inches=float(input("Enter your height inches:"))
height=height_feet*0.3048 + height_inches* 0.0254
bmi=weight/(height **2)
print("Your BMI is:",bmi)
if bmi >=18.5 and bmi<=24.9:
  print("You are in Normal weight✅\nGreat job! Your BMI is within the general healthy range. But remember, health is more than a number. Keep moving, eat well, sleep well, and continue building healthy habits.")
elif bmi <18.5:
  print("You are Underweight 🪶\nYour BMI is only a number, not your worth. Focus on becoming stronger and healthier, one step at a time. Nourish your body, build healthy habits, and be patient with yourself. Every small improvement matters!")
elif bmi >=25 and bmi <=29.9:
  print("You are Overweight⚠️\nYour BMI is only a number, not your identity. Don’t focus on being perfect—focus on becoming healthier, one small step at a time. Every healthy meal, every walk, and every good habit is progress. Keep going")
elif bmi >=30 :
  print("You are Obesity🛑\n💪 Your BMI is a number, not your identity.\nBeing in the obesity range doesn't mean you've failed—it simply means today is a good day to start taking care of yourself.\nYou don't need to change everything at once. Start with one small step: walk a little more, make one healthier choice, drink more water, or build one better habit.\nSmall steps + consistency = big changes.\nDon't compare yourself with others. Compare yourself with who you were yesterday.\n🌱Start where you are.\nDo what you can.\nKeep moving forward.Your journey isn't about becoming perfect.It\'s about becoming healthier, stronger, and happier—one day at a time.❤️")
print("Your number does not define you. What matters is the effort you make every day to become healthier, stronger, and better than yesterday. Start small. Stay consistent. Your future self will thank you.")