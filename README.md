# 💰 Gold Rate Prediction using Machine Learning and MLOps

An end-to-end machine learning project to predict gold prices based on USD to INR exchange rate. This project includes data cleaning, model training, serialization, deployment using Gradio, and automated logging to Google Sheets — demonstrating a complete MLOps pipeline.

---

## 🚀 Features

- 📊 **Data Analysis & Cleaning**  
  Handled missing values, cleaned and prepared the dataset for training.

- 🧠 **Model Building with Linear Regression**  
  Trained a regression model to predict gold rates based on the USD-INR value.

- ⚙️ **Hyperparameter Optimization**  
  Tuned model parameters to enhance prediction accuracy.

- 💾 **Model Serialization with Pickle**  
  Saved both the model and scaler for later inference.

- 🖥️ **Gradio Web Interface**  
  Built an interactive web UI to input USD-INR and get predicted gold rate.

- 📉 **Flagging & Logging**  
  Each prediction is optionally "flagged" and saved along with a timestamp.

- 📤 **Google Sheets Integration**  
  Automatically appends new flagged data into a Google Sheet for easy access and real-time updates.

---

## 🛠️ Technologies Used

| Tool/Library     | Purpose                          |
|------------------|----------------------------------|
| Python           | Programming language             |
| Pandas, NumPy    | Data manipulation                |
| scikit-learn     | Machine learning & preprocessing |
| Pickle           | Model serialization              |
| Gradio           | Web interface for prediction     |
| gspread & Google API | Append data to Google Sheets |
| Jupyter Notebook | Exploratory analysis             |
| VS Code          | Development environment          |

---



