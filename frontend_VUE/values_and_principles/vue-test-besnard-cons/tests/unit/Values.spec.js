import ValueItem from "../../src/components/ValueItem";
import Values from "../../src/components/Values";
import { createLocalVue, mount } from "@vue/test-utils";
import ValueEdit from "../../src/components/ValueEdit";

describe("Value component with 3 values", () => {
  const mockedValues = [
    { id: 1, title: "first Value" },
    { id: 2, title: "second Value" },
    { id: 3, title: "third Value" },
  ];
  const getValues = jest.fn().mockResolvedValue(mockedValues);

  const wrapper = mount(Values, {
    methods: { getValues },
  });

  test("contains 3 ValueItem components when we passed it through the props", () => {
    expect(wrapper.html()).toMatchSnapshot();
    expect(wrapper.html()).toContain(
      "First Value",
      "Second Value",
      "Third Value"
    );
    //another way to test it is by using the find methods in the child components because toContain is discouraged
    expect(wrapper.findAllComponents(ValueItem).length).toBe(3);
  });

  test("displays the add icon when we have less than 4 values", () => {
    expect(wrapper.html()).toContain('Click the "+" icon to add another value');
  });

  test("displays the edit component when clicking the plus icon", async () => {
    const plusButton = wrapper.find(".plus");
    await plusButton.trigger("click");

    const valueEditComponent = wrapper.findComponent(ValueEdit);
    expect(wrapper.vm.$data.editedValue).toEqual({ title: "" });
    expect(valueEditComponent.exists()).toBe(true);
  });

  async function getAndDisplayEditComponent() {
    wrapper.setData({ editedValue: { title: "" } });
    await wrapper.vm.$nextTick();
    const valueEditComponent = wrapper.findComponent(ValueEdit);
    return valueEditComponent;
  }

  test("passes the value to the local value when the user type in the input", async () => {
    const valueEditComponent = await getAndDisplayEditComponent();
    const textInput = valueEditComponent.find("input");

    textInput.element.value = "valueToAdd";
    await textInput.trigger("input");
    await valueEditComponent.vm.$nextTick();

    expect(valueEditComponent.vm.$data.localValue.title).toBe("valueToAdd");
  });

  test("calls the saveValue method when the user click on the save button", async () => {
    const valueEditComponent = await getAndDisplayEditComponent();
    const spy = jest.spyOn(valueEditComponent.vm, "saveValue");
    const saveButton = valueEditComponent.find("button");

    await saveButton.trigger("click");
    await valueEditComponent.vm.$nextTick();

    expect(spy).toHaveBeenCalled();
  });
});

describe("Value component with 4 values", () => {
  const localVue = createLocalVue();
  const mockedValues = [
    { id: 1, title: "first Value" },
    { id: 2, title: "second Value" },
    { id: 3, title: "third Value" },
    { id: 4, title: "forth Value" },
  ];
  const getValues = jest.fn().mockResolvedValue(mockedValues);

  const wrapper = mount(Values, {
    methods: { getValues },
    localVue: localVue,
  });

  test("doesn't display the add icon or the edit component when we have 4 values", () => {
    expect(wrapper.html()).not.toContain(
      'Click the "+" icon to add another value'
    );
    const ValueEditComponent = wrapper.findComponent(ValueEdit);
    expect(ValueEditComponent.exists()).toBe(false);
  });

  test("displays the Value Edit component when we click the edit icon and placeholder has the value already written", async () => {
    const ValueItems = wrapper.findAllComponents(ValueItem);
    const spy = jest.spyOn(wrapper.vm, "valueEdit");
    await ValueItems.at(1).vm.$emit("ValueEdit", 2);
    expect(spy).toHaveBeenCalled();
    await wrapper.vm.$nextTick();
    const ValueEditComponent = wrapper.findComponent(ValueEdit);
    expect(ValueEditComponent.exists()).toBe(true);
    const textInput = ValueEditComponent.find("input").element.value;
    expect(textInput).toBe("second Value");
  });
});
