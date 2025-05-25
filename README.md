# Food Data Exploration and Classification

This project is a two-part exploration of food datasets, combining structured nutritional data analysis with deep learning for visual food classification.

---

## Part 1: Nutrient Dashboard with Streamlit

`app.py`, this interactive app allows you to:

- Load and explore USDA Food and Nutrient Database data (CSV) (https://fdc.nal.usda.gov/)
- Analyze nutrient values across various food ingredients
- Visualize nutrient distributions using Plotly and Seaborn
- Demonstrate how structured historical data supports real-time sensor analytics

This section showcases how food data is **collected, cleaned, and analyzed** across different platforms. It lays the foundation for **streamlined pipelines**, depending on how the data is acquired and used.

---

## Part 2: Food Image Classification (Mini Example)

`image_classification_101_dataset.ipynb`, this notebook demonstrates:

- Loading image data from the [Food-101 dataset](https://data.vision.ee.ethz.ch/cvl/food-101/)
- Selecting only **3 food categories** (`apple_pie`, `cheese_plate`, `donuts`) as a simplified demo
- Building and training a basic CNN model using PyTorch
- Evaluating the model with a **confusion matrix** and visualizing **misclassified examples**

### 🛠 Technologies Used

- PyTorch, Torchvision
- Matplotlib for performance visualization
- ImageFolder, DataLoader for batch management

---

## 🔍 Why This Project?

This hybrid project demonstrates:

- How food-related data comes in multiple forms (structured vs. unstructured)
- How to explore and visualize nutrient properties for food quality assessment
- How to build a foundational deep learning model for image classification
- How such tools can be extended to **food quality control**, **supply chains**, and **AI-driven product development**

---

## 🚀 Future Improvements

- Integrate pretrained models like `ResNet18`, `EfficientNet` for improved accuracy
- Add precision, recall, and Grad-CAM visualizations for explainability
- Connect nutrient insights with food image predictions for a unified pipeline
- Extend the dataset to **sensor-based food data** and evaluate properties such as:
  - Article freshness
  - Nutritional degradation
  - Ingredient suitability

These approaches are already being implemented in:

- Smart irrigation systems for automated farming and data logging  
- Conveyor belt and transportation systems for weight calibration and defect detection  
- IoT-powered food industry setups to optimize ingredient ratios and automation  
- Nutritional product development (juices, dietary supplements, etc.) based on data-driven insights

 
P.S: Due to dataset size constraints, only 3 class folders (`apple_pie`, `cheese_plate`, `donuts`) are included under `food-101/images/`.  
This classification is intended as a **conceptual demonstration** of deep learning on food imagery.
