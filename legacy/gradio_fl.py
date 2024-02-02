import gradio as gr

def lava_chatbot(image, question):
    # 这里应该是调用 LLaVA 模型或其他模型的代码
    # 下面是一个假设的占位函数
    response = "这是对你的提问的响应。"  # 实际的响应应来自模型
    return response

iface = gr.Interface(
    fn=lava_chatbot,
    inputs=[
        gr.inputs.Image(type="pil", label="上传图片"),  # PIL 图像类型输入
        gr.inputs.Textbox(label="输入问题")  # 文本输入
    ],
    outputs=[
        gr.outputs.Textbox(label="LLaVA Chatbot 回答")  # 文本输出
    ],
    title="LLaVA: Large Language and Vision Assistant",
    description="上传图片并输入问题，LLaVA Chatbot 将提供回答。"
)

if __name__ == "__main__":
    iface.launch()
