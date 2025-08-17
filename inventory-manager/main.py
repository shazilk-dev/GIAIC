import asyncio
import os
from dotenv import load_dotenv
from openai import AsyncOpenAI
from agents import Agent,Runner, function_tool, OpenAIChatCompletionsModel, set_tracing_disabled

load_dotenv()

GEMINI_MODEL: str = os.getenv("GEMINI_MODEL")
GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY")
BASE_URL: str = os.getenv("BASE_URL")


client: AsyncOpenAI = AsyncOpenAI(
    api_key = GEMINI_API_KEY,
    base_url = BASE_URL    
)

model: OpenAIChatCompletionsModel = OpenAIChatCompletionsModel(
    model=GEMINI_MODEL,
    openai_client=client
)
set_tracing_disabled(disabled=True)


inventory = [
    {"id": 1, "name": "T-Shirt", "category": "clothing", "quantity": 25, "price": 19.99},
    {"id": 2, "name": "Jeans", "category": "clothing", "quantity": 15, "price": 49.99},
    {"id": 3, "name": "Sneakers", "category": "footwear", "quantity": 10, "price": 79.99},
    {"id": 4, "name": "Laptop", "category": "electronics", "quantity": 5, "price": 899.99},
    {"id": 5, "name": "Coffee Mug", "category": "kitchenware", "quantity": 30, "price": 12.99}
]

def get_next_id():
    """Get the next available ID for new products"""
    if not inventory:
        return 1
    return max(item["id"] for item in inventory) + 1

@function_tool
def inventory_manager(operation: str, name: str = None, category: str = None, 
                     quantity: int = None, price: float = None, 
                     new_name: str = None, new_category: str = None) -> str:
    """
    Handles all inventory operations based on operation parameter.
    Operations: add, remove, update, show, info, update_quantity
    """
    try:
        operation = operation.lower().strip()
        
        if operation == "add":
            # Add new product
            if not all([name, category, quantity is not None, price is not None]):
                return "For 'add' operation: name, category, quantity, and price are required"
            
            new_product = {
                "id": get_next_id(),
                "name": name.strip(),
                "category": category.strip().lower(),
                "quantity": int(quantity),
                "price": float(price)
            }
            inventory.append(new_product)
            return f"Successfully added {name} to inventory with ID {new_product['id']}"
        
        elif operation == "remove":
            # Remove product
            if not name:
                return "For 'remove' operation: name is required"
            
            product_to_remove = next((item for item in inventory if item["name"].lower() == name.lower().strip()), None)
            if product_to_remove:
                inventory.remove(product_to_remove)
                return f"Successfully removed {product_to_remove['name']} from inventory"
            else:
                return f"Product '{name}' not found in inventory"
        
        elif operation == "update":
            # Update product details
            if not name:
                return "For 'update' operation: name is required"
            
            product_to_update = next((item for item in inventory if item["name"].lower() == name.lower().strip()), None)
            if not product_to_update:
                return f"Product '{name}' not found in inventory"
            
            # Update fields if provided
            if new_name:
                product_to_update["name"] = new_name.strip()
            if new_category:
                product_to_update["category"] = new_category.strip().lower()
            if quantity is not None:
                product_to_update["quantity"] = int(quantity)
            if price is not None:
                product_to_update["price"] = float(price)

            return f"Successfully updated {product_to_update['name']}"
        
        elif operation == "show":
            # Show products
            products_to_show = inventory
            
            if category:
                products_to_show = [item for item in inventory if item["category"].lower() == category.lower().strip()]
            elif name:
                products_to_show = [item for item in inventory if name.lower().strip() in item["name"].lower()]
            
            if not products_to_show:
                return "No products found matching your criteria"
            
            result = "INVENTORY PRODUCTS:\n" + "="*50 + "\n"
            for product in products_to_show:
                result += f"ID: {product['id']} | Name: {product['name']} | Category: {product['category']}\n"
                result += f"Quantity: {product['quantity']} | Price: ${product['price']:.2f}\n"
                result += "-" * 50 + "\n"
            
            return result
        
        elif operation == "info":
            # Get product info
            if not name:
                return "For 'info' operation: name is required"
            
            product = next((item for item in inventory if item["name"].lower() == name.lower().strip()), None)
            if not product:
                return f"Product '{name}' not found in inventory"
            
            return f"""PRODUCT DETAILS:
                        Name: {product['name']}
                        ID: {product['id']}
                        Category: {product['category']}
                        Quantity: {product['quantity']}
                        Price: ${product['price']:.2f}
                        Total Value: ${product['quantity'] * product['price']:.2f}"""
        
        elif operation == "update_quantity":
            # Update quantity
            if not name or quantity is None:
                return "For 'update_quantity' operation: name and quantity are required"
            
            product_to_update = next((item for item in inventory if item["name"].lower() == name.lower().strip()), None)
            if not product_to_update:
                return f"Product '{name}' not found in inventory"
            
            product_to_update["quantity"] = int(quantity)
            return f"Successfully updated {product_to_update['name']} quantity to {quantity}"
        
        else:
            return f"Unknown operation '{operation}'. Available operations: add, remove, update, show, info, update_quantity"

    except Exception as e:
        return f"Error in {operation} operation: {str(e)}"

agent = Agent(
    name="Inventory Manager",
    model=model,
    instructions="""You are a helpful inventory management assistant. You have ONE main tool: inventory_manager.

            This tool handles ALL operations based on the 'operation' parameter:

            1. **add** - Add new product (requires: name, category, quantity, price)
            2. **remove** - Remove product (requires: name)  
            3. **update** - Update product details (requires: name, optional: new_name, new_category, quantity, price)
            4. **show** - Show products (optional: category or name for filtering)
            5. **info** - Get product details (requires: name)
            6. **update_quantity** - Update quantity only (requires: name, quantity)

            Always be friendly and provide clear confirmations. Handle natural language requests like:
            - "Add 20 t-shirts in clothing category at $15 each" → use operation="add"
            - "Show me all clothing items" → use operation="show" with category="clothing"
            - "Remove the laptop" → use operation="remove" with name="laptop"
            - "Update t-shirt quantity to 30" → use operation="update_quantity"
            - "What's the price of sneakers?" → use operation="info"

            Be conversational and helpful!""",
    tools=[inventory_manager]
            )

async def main():
    """Main function to run the inventory agent"""
    
    print("Inventory Management Agent Ready!")
    print("You can ask me to add, remove, update products, show inventory, etc.")
    print("Type 'quit' to exit\n")
    
    runner = Runner()
    
    while True:
        user_input = input("\n👤 You: ").strip()

        print(inventory)
        
        if user_input.lower() in ['quit', 'exit', 'bye']:
            print("Goodbye!")
            break
        
        if not user_input:
            continue
        
        try:
            result = await runner.run(starting_agent=agent, input=user_input)
            print(f"\nAgent: {result.final_output_as(str)}")
            
        except Exception as e:
            print('exception')
            print(f"Error: {e}")

if __name__ == "__main__":
    asyncio.run(main())